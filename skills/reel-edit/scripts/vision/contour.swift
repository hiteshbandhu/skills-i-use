import Foundation
import Vision
import ImageIO
// usage: contour <image> <out.json>
let a=CommandLine.arguments
let s=CGImageSourceCreateWithURL(URL(fileURLWithPath: a[1]) as CFURL,nil)!; let cg=CGImageSourceCreateImageAtIndex(s,0,nil)!
var paths:[[[Double]]]=[]
for (ca,dark) in [(3.0,true),(3.0,false),(1.5,true)] {
let req=VNDetectContoursRequest(); req.contrastAdjustment=Float(ca); req.detectsDarkOnLight=dark; req.maximumImageDimension=2048
try VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
if let o=req.results?.first { for c in o.topLevelContours { func walk(_ c:VNContour){ let p=c.normalizedPoints; if p.count>8 { paths.append(p.map{[Double($0.x)*1080,Double(1-$0.y)*1920]}) }; for ch in c.childContours { walk(ch) } }; walk(c) } } }
try JSONSerialization.data(withJSONObject: paths).write(to: URL(fileURLWithPath: a[2])); print("contours",paths.count,paths.reduce(0){$0+$1.count})
