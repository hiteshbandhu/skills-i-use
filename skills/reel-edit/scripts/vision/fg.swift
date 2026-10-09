import Foundation
import Vision
import CoreImage
import ImageIO
import UniformTypeIdentifiers
// usage: fg <inDir> <outDir> [step]  -> foreground (all instances) matte PNG
let a=CommandLine.arguments; let inDir=a[1], outDir=a[2]; let step=a.count>3 ? Int(a[3])! : 1
try? FileManager.default.createDirectory(atPath: outDir, withIntermediateDirectories: true)
let files=try FileManager.default.contentsOfDirectory(atPath: inDir).filter{$0.hasSuffix(".jpg")}.sorted()
let ctx=CIContext(); var n=0
for (i,f) in files.enumerated() where i % step == 0 {
  let url=URL(fileURLWithPath: inDir+"/"+f)
  guard let src=CGImageSourceCreateWithURL(url as CFURL,nil), let cg=CGImageSourceCreateImageAtIndex(src,0,nil) else {continue}
  let req=VNGenerateForegroundInstanceMaskRequest()
  let h=VNImageRequestHandler(cgImage: cg, options: [:])
  do { try h.perform([req]) } catch { print("err",error); continue }
  guard let obs=req.results?.first else { continue }
  guard let pb=try? obs.generateScaledMaskForImage(forInstances: obs.allInstances, from: h) else {continue}
  let ci=CIImage(cvPixelBuffer: pb)
  let outURL=URL(fileURLWithPath: outDir+"/"+f.replacingOccurrences(of: ".jpg", with: ".png"))
  if let o=ctx.createCGImage(ci, from: ci.extent), let d=CGImageDestinationCreateWithURL(outURL as CFURL, UTType.png.identifier as CFString, 1, nil) { CGImageDestinationAddImage(d,o,nil); CGImageDestinationFinalize(d); n+=1 }
}
print("done",n)
