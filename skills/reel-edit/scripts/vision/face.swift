import Foundation
import Vision
import ImageIO
// usage: face <inDir> <out.json> [step]  -> {"0000": [[x,y,w,h],...]} in image pixels (top-left origin)
let a=CommandLine.arguments; let inDir=a[1], outPath=a[2]; let step=a.count>3 ? Int(a[3])! : 1
let files=try FileManager.default.contentsOfDirectory(atPath: inDir).filter{$0.hasSuffix(".jpg")}.sorted()
var out:[String:[[Double]]]=[:]
for (i,f) in files.enumerated() where i % step == 0 {
  guard let s=CGImageSourceCreateWithURL(URL(fileURLWithPath: inDir+"/"+f) as CFURL,nil), let cg=CGImageSourceCreateImageAtIndex(s,0,nil) else { continue }
  let req=VNDetectFaceRectanglesRequest(); try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
  let W=Double(cg.width), H=Double(cg.height)
  out[String(f.dropLast(4))]=(req.results ?? []).map{ let b=$0.boundingBox; return [Double(b.minX)*W, Double(1-b.maxY)*H, Double(b.width)*W, Double(b.height)*H] }
}
try JSONSerialization.data(withJSONObject: out).write(to: URL(fileURLWithPath: outPath)); print("faces", out.count, out.values.filter{!$0.isEmpty}.count)
