---
type: concept
title: "CIE Color Matching Functions"
created: 2026-06-05
updated: 2026-06-05
tags:
  - color-science
  - cie
  - color-matching
  - color-standards
status: seed
related:
  - "[[Color Metamerism]]"
  - "[[DaVinci 色彩管理]]"
  - "[[DaVinci 色彩空间与 ACES]]"
sources:
  - "[[Advanced Color Science Course 2026]]"
---

# CIE Color Matching Functions (CIE CMF)

## Overview

Color Matching Functions (CMF) are spectral response curves that define how a standardized observer perceives light across the visible spectrum (380-780 nm). The CIE (International Commission on Illumination) defines these functions for standardized observers used in color measurement and specification.

## Standard Observers

### CIE 1931 Standard Observer (2° Standard Observer)

**Specification:**
- **Viewing Angle:** 2° field of view
- **Visual Area:** ~0.3mm² at 1 meter viewing distance
- **Retinal Distribution:** Foveal cone cells only (no rod cells)
- **Basis:** Color matching experiments by Guild (1931) and Wright (1928)

**Characteristics:**
- Most widely used standard observer
- Good for small object color matching
- Used in ACES standard and professional color grading workflows
- Wavelength Range: 380-780 nm with 5 nm steps

**CMF Values (x̄, ȳ, z̄):**
The three curves represent the sensitivity of the three cone types (roughly corresponding to red, green, blue):
- **x̄ (Red):** Peaks at ~700 nm
- **ȳ (Green):** Peaks at ~546 nm (luminosity function)
- **z̄ (Blue):** Peaks at ~436 nm

### CIE 1964 Supplementary Observer (10° Standard Observer)

**Specification:**
- **Viewing Angle:** 10° field of view
- **Visual Area:** Larger field including peripheral retina
- **Retinal Distribution:** Mix of cone and rod cells
- **Basis:** Color matching experiments with larger visual fields

**Key Differences from CIE 1931:**
- Includes rod cell response at low luminance levels
- Different spectral sensitivities, especially in blue region
- Better represents peripheral vision color response
- Larger viewing angle matches many practical viewing situations

**When to Use:**
- Large object/display viewing (cinema screens, large monitors)
- Peripheral vision critical to task
- Applications requiring rod cell contribution

## Physiological Variation (生理CMF)

### Individual Differences
- **Natural Variation:** Real human observers have slightly different CMF from the standardized values
- **Cone Pigment Variation:** Spectral absorption of cone pigments varies ±10-15% across population
- **Yellow Channel Sensitivity:** Most significant individual variation is in yellow region
- **Age Effects:** CMF changes with age (lens yellowing, photoreceptor density changes)

### Practical Implications for Color Workflows
- **Color Matching Tolerance:** No two observers will perfectly agree on color match
- **Industry Standards:** Professional workflows accept ±10 Delta-E as acceptable color matching tolerance
- **Observer Pool:** Color grading reviews should involve multiple observers to catch metamerism

## Relationship to ACES

### ACES Derivation
- ACES 1.0 standard uses CIE 1931 standard observer as the basis
- All IDT (Input Device Transform) and ODT (Output Device Transform) design assumes CIE 1931 CMF
- Color space matrix definitions reference CIE 1931 primaries

### Implications
- Mastering in ACES/DaVinci under CIE 1931 assumption
- Final theatrical delivery (DCP) also assumes CIE 1931 observer for consistency
- Streaming delivery to different devices may have different effective CMF due to device spectral response

## Measurement and Application

### Colorimetry Calculations
```
X = ∫ Φ(λ) × x̄(λ) dλ
Y = ∫ Φ(λ) × ȳ(λ) dλ
Z = ∫ Φ(λ) × z̄(λ) dλ
```

Where Φ(λ) is the spectral power distribution of the light source.

### CIE XYZ Color Space
- Derived from CMF integration
- Foundation for all modern color spaces (sRGB, Lab, etc.)
- Used in professional color measurement

### Monitor Calibration
- Professional monitors are calibrated to approximate CIE standard observer response
- Calibration includes CMF matching to ensure consistent color appearance
- Different observer assumptions can create calibration conflicts

## Color Matching Failure Cases

When color matching *fails* despite identical apparent color under one condition:

1. **Different Illuminants:** Two samples with different SPDs may look identical under Daylight (D65) but different under Tungsten (A)
2. **Different Observers:** Color match verified by one observer (CIE 1931) may fail for another observer or under CIE 1964 conditions
3. **Device vs Human:** Camera-verified color match may not match human perception due to different CMF

See [[Color Metamerism]] for detailed discussion.

## Related Standards

- **CIE 1976 Lab/Luv:** Perceptually uniform spaces derived from CIE XYZ and 1931 CMF
- **CIE 2015 Standard Daylight Illuminants:** D65, D50, etc. referenced with standard observer
- **ISO 3664 Lighting for Color Assessment:** Specifies illumination conditions and observer model for professional color evaluation

## References

- **Foundation:** CIE 15:2004 *Colorimetry*, 3rd Edition
- **ACES:** Academy Color Encoding System reference documentation
- **Professional Use:** ISO 3664 (color evaluation lighting), ISO 12640 (color image quality)
