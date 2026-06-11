---
type: concept
title: "Color Metamerism"
created: 2026-06-05
updated: 2026-06-05
tags:
  - color-science
  - color-matching
  - metamerism
status: seed
related:
  - "[[DaVinci 色彩管理]]"
  - "[[DaVinci 色彩空间与 ACES]]"
  - "[[Advanced Color Science Course 2026]]"
sources:
  - "[[Advanced Color Science Course 2026]]"
---

# Color Metamerism (同色异谱)

## Definition

Metamerism occurs when two samples that appear the same color under one illuminant or viewing condition appear different under another illuminant or viewing condition, despite having different spectral power distributions (SPDs).

This is the inverse of **metameric failure** (同色异谱失效), where samples that *should* match fail to match due to SPD differences.

## Physical Causes

### Light Source Effects
- **Spectral Composition Mismatch:** Two original samples may have identical color appearance under one light source's spectrum
- **Distribution Shift:** When the illuminant spectrum changes, the different SPDs of the original samples respond differently
- **Mismatch Result:** What appeared identical becomes visibly different

### Observer Differences

#### Physiological (Human Observer)
- **Individual Variation:** Each human retina has slightly different cone cell spectral response
- **生理CMF (Physiological Color Matching Function):** Each individual's CMF differs from the standard CIE observer
- **Small but Measurable:** Typically ±10-15% variation from standard values
- **Yellow Channel Sensitivity:** Yellow color saturation density varies significantly across individuals

#### Instrumental (Device/Camera Observer)
- **CMF Characteristics:** Cameras, scanners, and imaging devices have device-specific color response curves
- **Standards Mismatch:** Equipment CMF may differ substantially from CIE standard observer
- **Workflow Impact:** A color match verified by human eye may fail when imaged by a camera with different spectral response

#### Viewing Geometry
- **CIE 1931 Standard Observer:**
  - 2° viewing angle (small field)
  - Equivalent to ~0.3mm² viewing area at 1 meter
  - Uses foveal cone distribution
  
- **CIE 1964 Supplementary Observer:**
  - 10° viewing angle (large field)
  - Includes peripheral retinal sensitivity
  - Different cone and rod distribution
  
- **Consequence:** Colors may appear to match under one viewing angle but mismatch under another angle, or match to one observer but not another

## Professional Impact in Color Workflows

### DaVinci Resolve / ACES Workflows
- **Observer Selection:** ACES IDT/ODT design assumes CIE 1931 standard observer
- **Color Space Design:** Metamerism considerations affect whether transformations preserve perceived color across observers
- **Monitor Calibration:** Professional monitors are calibrated to standard observer models, which may not match all human viewers exactly

### Cinema Mastering (DCP/IMF)
- **Theatrical Display:** Cinema screens use specific illuminants (e.g., X25 white point)
- **Color Matching Across Platforms:** A DCP mastered under one observer model may require different grading if final delivery is to streaming (different viewing conditions, observer demographics)
- **KDM + Decryption:** Ensures mastered grade is preserved during theatrical exhibition, but metamerism still occurs during grade creation

## How to Account for Metamerism

1. **Test under multiple illuminants** — view color grades under daylight, tungsten, and LED lighting
2. **Use standard observers consistently** — declare whether you're using CIE 1931 (2°) or CIE 1964 (10°)
3. **Verify on target display device** — confirm color match on the actual cinema screen, broadcast monitor, or streaming delivery device
4. **Document observer assumptions** — in DCP metadata and mastering reports
5. **Use spectrophotometric verification** — measure actual SPD rather than relying only on visual assessment

## Related Concepts

- [[CIE Color Matching Functions]] — quantifies standard observer color response
- [[DaVinci 色彩管理]] — practical color management in DaVinci Resolve
- [[DCP 母版制作]] — DCP mastering considers metamerism in final delivery verification
