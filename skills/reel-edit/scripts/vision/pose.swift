import Foundation
import Vision
import ImageIO
// usage: pose <inDir> <out.json>
let a=CommandLine.arguments; let inDir=a[1], outPath=a[2]
let files=try FileManager.default.contentsOfDirectory(atPath: inDir).filter{$0.hasSuffix(".jpg")}.sorted()
var out:[[[String:[Double]]]]=[]
for f in files {
  let s=CGImageSourceCreateWithURL(URL(fileURLWithPath: inDir+"/"+f) as CFURL,nil)!; let cg=CGImageSourceCreateImageAtIndex(s,0,nil)!
  let req=VNDetectHumanBodyPoseRequest(); let h=VNImageRequestHandler(cgImage: cg, options: [:]); try? h.perform([req])
  var people:[[String:[Double]]]=[]
  for o in req.results ?? [] {
    var d:[String:[Double]]=[:]
    if let pts=try? o.recognizedPoints(.all) { for (k,p) in pts where p.confidence>0.2 { d[k.rawValue.rawValue]=[Double(p.location.x)*1080,Double(1-p.location.y)*1920,Double(p.confidence)] } }
    people.append(d)
  }
  out.append(people)
}
try JSONSerialization.data(withJSONObject: out).write(to: URL(fileURLWithPath: outPath)); print("pose",out.count,out.filter{!$0.isEmpty}.count)
