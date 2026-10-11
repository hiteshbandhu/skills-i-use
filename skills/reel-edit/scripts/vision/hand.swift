import Foundation
import Vision
import ImageIO
// usage: hand <inDir> <out.json>
let a=CommandLine.arguments; let inDir=a[1], outPath=a[2]
let files=try FileManager.default.contentsOfDirectory(atPath: inDir).filter{$0.hasSuffix(".jpg")}.sorted()
let req=VNDetectHumanHandPoseRequest(); req.maximumHandCount=4
let joints:[VNHumanHandPoseObservation.JointName]=[.thumbTip,.indexTip,.middleTip,.ringTip,.littleTip,.wrist,.indexMCP]
let names=["thumb","index","middle","ring","little","wrist","indexMCP"]
var out:[[[String:Any]]]=[]
for f in files {
  let url=URL(fileURLWithPath: inDir+"/"+f)
  guard let src=CGImageSourceCreateWithURL(url as CFURL,nil), let cg=CGImageSourceCreateImageAtIndex(src,0,nil) else { out.append([]); continue }
  let h=VNImageRequestHandler(cgImage: cg, options: [:]); try? h.perform([req])
  var hands:[[String:Any]]=[]
  for obs in req.results ?? [] {
    var d:[String:Any]=["c":obs.confidence]
    for (j,n) in zip(joints,names) { if let p=try? obs.recognizedPoint(j), p.confidence>0.3 { d[n]=[Double(p.location.x)*1080, Double(1-p.location.y)*1920, Double(p.confidence)] } }
    hands.append(d)
  }
  out.append(hands)
}
let data=try JSONSerialization.data(withJSONObject: out)
try data.write(to: URL(fileURLWithPath: outPath))
print("frames",out.count,"withHands",out.filter{!$0.isEmpty}.count)
