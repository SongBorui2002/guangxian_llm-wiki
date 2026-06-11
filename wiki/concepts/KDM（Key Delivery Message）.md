---
type: concept
title: "KDM（Key Delivery Message）"
created: 2026-06-05
updated: 2026-06-05
tags:
  - transkoder
  - dcp
  - encryption
  - security
status: seed
related:
  - "[[DCP 母版制作]]"
  - "[[CPL（Composition Playlist）]]"
sources:
  - "[[Transkoder 2025 用户指南]]"
complexity: intermediate
domain: "transkoder"
aliases:
  - "Key Delivery Message"
  - "密钥分发消息"
---

# KDM（Key Delivery Message）

**KDM**（Key Delivery Message，密钥分发消息）用于将加密 DCP 的解密密钥分发给授权的影院设备。

## 工作原理

1. 内容制作者在 Transkoder 中创建加密的 DCP 包
2. 生成 KDM，将解密密钥绑定到目标影院设备的数字证书
3. KDM 只能被指定设备使用，无法在其他设备上解密内容

## Transkoder 中的 KDM 生成

在 DCP Finalize 窗口的 **DCP KDM** 选项卡中配置：

| 参数 | 说明 |
|------|------|
| **目标设备** | 指定影院的放映服务器证书 |
| **有效期** | KDM 的有效时间窗口 |
| **水印** | 可选 Nagra NexGuard 取证水印嵌入 |
| **音频/字幕权限** | 控制可用音轨和字幕 |

## 安全注意事项

- KDM 文件本身是加密的，只能被目标设备读取
- NexGuard 取证水印可追踪盗录源
- 4K 水印编码保持高性能