# N8N Templates Library - Brand Assets & Visual Identity Package

> **Category**: Automation  
> **Asset Version**: 1.0.0 (Production Release)  
> **Primary Brand Color**: `#3B82F6` | **Accent**: `#8B5CF6` | **Background**: `#0F172A`

## 📦 Package Manifest
| Asset Name | Format | Dimensions | Usage |
| :--- | :---: | :---: | :--- |
| `logo_primary.svg` | Vector SVG | 320x80 | Primary horizontal lockup for headers, navigation, splash screens |
| `logo_symbol.svg` | Vector SVG | 128x128 | Brand mark, squircle icon, mobile app mark |
| `logo_monochrome_white.svg` | Vector SVG | 320x80 | High-contrast white logo for dark surfaces and photo overlays |
| `logo_monochrome_black.svg` | Vector SVG | 320x80 | High-contrast black logo for light surfaces and monochrome print |
| `ic_launcher_foreground.svg`| Vector SVG | 108x108 | Android Adaptive Icon Foreground layer |
| `ic_launcher_background.svg`| Vector SVG | 108x108 | Android Adaptive Icon Background layer |
| `favicon.svg` | Vector SVG | 32x32 | Modern browser tab favicon (Scalable) |
| `logo_primary.png` | Raster PNG | 2x Scaled | High-DPI transparent PNG logo |
| `logo_symbol.png` | Raster PNG | 512x512 | High-DPI square brand icon |
| `favicon-512x512.png` | Raster PNG | 512x512 | PWA Splash Screen & App Store Icon |
| `favicon-192x192.png` | Raster PNG | 192x192 | Android PWA homescreen icon |
| `favicon-32x32.png` | Raster PNG | 32x32 | Standard desktop browser favicon |
| `favicon-16x16.png` | Raster PNG | 16x16 | Compact browser tab favicon |

## 🚀 Code Integration Guide

### 1. Flutter Mobile / Desktop
```yaml
# pubspec.yaml
flutter:
  assets:
    - assets/brand/logo_primary.png
    - assets/brand/logo_symbol.png
```
```dart
// Dart Widget
Image.asset('assets/brand/logo_primary.png', height: 40);
```

### 2. Web HTML / Next.js / Vite
```html
<!-- index.html -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/favicon-192x192.png">
```

### 3. Android Adaptive Launcher (`mipmap-anydpi-v26/ic_launcher.xml`)
```xml
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_launcher_foreground" />
</adaptive-icon>
```
