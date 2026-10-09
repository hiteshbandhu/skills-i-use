import Foundation
import Vision
import CoreImage
import ImageIO
import UniformTypeIdentifiers
// usage: seg <inDir> <outDir> [step]
let args=CommandLine.arguments; let inDir=args[1], outDir=args[2]; let step=args.count>3 ? Int(args[3])! : 1
try? FileManager.default.createDirectory(atPath: outDir, withIntermediateDirectories: true)
let files=try FileManager.default.contentsOfDirectory(atPath: inDir).filter{$0.hasSuffix(".jpg")}.sorted()
let ctx=CIContext()
let req=VNGeneratePersonSegmentationRequest(); req.qualityLevel = .accurate; req.outputPixelFormat = kCVPixelFormatType_OneComponent8
var n=0
for (i,f) in files.enumerated() where i % step == 0 {
  let url=URL(fileURLWithPath: inDir+"/"+f)
  guard let src=CGImageSourceCreateWithURL(url as CFURL,nil), let cg=CGImageSourceCreateImageAtIndex(src,0,nil) else {continue}
  let h=VNImageRequestHandler(cgImage: cg, options: [:])
  do { try h.perform([req]) } catch { print("err",f); continue }
  guard let pb=req.results?.first?.pixelBuffer else {continue}
  var ci=CIImage(cvPixelBuffer: pb)
  let sx=CGFloat(cg.width)/ci.extent.width, sy=CGFloat(cg.height)/ci.extent.height
  ci=ci.transformed(by: CGAffineTransform(scaleX: sx, y: sy))
  let outURL=URL(fileURLWithPath: outDir+"/"+f.replacingOccurrences(of: ".jpg", with: ".png"))
  if let o=ctx.createCGImage(ci, from: CGRect(x:0,y:0,width:cg.width,height:cg.height)),
     let d=CGImageDestinationCreateWithURL(outURL as CFURL, UTType.png.identifier as CFString, 1, nil) { CGImageDestinationAddImage(d,o,nil); CGImageDestinationFinalize(d); n+=1 }
}
print("done",n)
