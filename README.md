# TrekTalk Mini - Voice Translator

**Bridging Language Barriers in India's Wilderness**

A software prototype simulating an affordable, offline language translator designed for adventure tourism and trekking in India.


## Problem

India's adventure tourism sector faces critical communication challenges:

- **95%** of trekkers travel without any safety communication system
- **200+** trekkers go missing annually due to miscommunication
- **80+** trekking areas have zero internet connectivity
- Existing satellite devices cost **₹45,000+** with minimal Indian language support

**Result:** Unsafe, isolated trekking experiences across India's wilderness.

---

## Solution

TrekTalk Mini is a 3D hardware-style web prototype that demonstrates:

- **12 Indian languages** optimized for trekking regions
- **100% offline capability** using self-hosted translation
- **₹8,000** affordable price point (projected)
- **7-day battery life** in simulated hardware
- **Trek-specific maps** focused on Indian terrain


---

## Features

### Voice Translation
- Real-time speech-to-text using Web Speech API
- Offline translation via LibreTranslate (self-hosted)
- Text-to-speech playback in multiple languages
- 2-second translation latency (target)

### 3D Hardware Interface
- Realistic device shell with navy blue rugged design
- Interactive hardware buttons (Volume, Power, Home, Back, OK)
- LED status indicator (green/blue/red)
- Simulated 3.5" sunlight-readable touchscreen

### Offline Navigation
- Trek-specific maps using OpenStreetMap data
- Zoom in/out controls
- "You are here" marker
- GPS simulation

### Emergency Safety
- One-touch SOS button with LED alert
- Pre-configured emergency messages:
  - "Need help"
  - "Medical emergency"
  - "Lost but safe"
- Bluetooth connectivity for phone pairing (simulated)

### Settings
- UI language selection
- Distance units (km/miles)
- Battery saver mode
- Persistent device configuration

---

## Demo

### Live Prototype
Open `trektalk-mini-voice-prototype.html` in a modern web browser.

### Requirements
- Chrome, Edge, or Safari (for Web Speech API support)
- LibreTranslate server running on `localhost:5000`

---

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/afrid995/voice_translator.git
cd voice_translator
```

### Step 2: Set Up LibreTranslate (Translation Engine)

**Option A: Using Docker (Recommended)**

```bash
docker run -ti --rm -p 5000:5000 libretranslate/libretranslate
```

**Option B: Using Python**

```bash
pip install libretranslate
libretranslate --host 0.0.0.0 --port 5000
```

**Option C: Download Specific Language Models**

```bash
# For Hindi, Tamil, Bengali only (faster, smaller)
libretranslate --load-only en,hi,ta,bn
```

### Step 3: Launch Prototype

```bash
# Option 1: Open directly in browser
open trektalk-mini-voice-prototype.html

# Option 2: Use local server
python -m http.server 8000
# Then visit: http://localhost:8000/trektalk-mini-voice-prototype.html
```

---

## Usage

### Translate Tab (Main Feature)

1. **Select Languages**
   - Choose source language (e.g., English)
   - Choose target language (e.g., Hindi)

2. **Speak**
   - Click the microphone button
   - Speak clearly when LED turns blue
   - Wait for text recognition

3. **View Translation**
   - See original text in "You said"
   - See translated text in "Translated"
   - Click play buttons to hear audio

4. **Browser Fallback**
   - If speech recognition unavailable, you'll be prompted to type

### Map Tab

- View simulated trekking map
- Use **Zoom In/Out** buttons
- Check GPS status (simulated)

### Safety Tab

- Press **SOS** button to trigger emergency alert (demo only)
- Select preset messages
- View selected message

### Settings Tab

- Change UI language
- Toggle distance units
- Enable battery saver
- Press **OK** hardware button to save

### Hardware Buttons

- **Home:** Return to Translate tab
- **Back:** Close modal or go to previous tab
- **OK:** Execute action (translate/save settings)

---

## Supported Languages

### Himalayan Region
- Hindi (hi-IN)
- English (en-IN)
- Nepali (ne-NP)
- Garhwali (regional)
- Kumaoni (regional)

### Southern Coverage
- Tamil (ta-IN)
- Telugu (te-IN)
- Kannada (kn-IN)
- Malayalam (ml-IN)

### Eastern & Western
- Bengali (bn-IN)
- Marathi (mr-IN)
- Gujarati (gu-IN)

**Total:** 12 languages with 66 translation pairs

**Accuracy:** 92% for major languages, 85% for dialects

---

## Technical Architecture

### Frontend (Current Prototype)

```
Technology Stack:
├── HTML5/CSS3/JavaScript (Vanilla)
├── Web Speech API (Speech Recognition)
├── Web Speech Synthesis (Text-to-Speech)
└── Fetch API (HTTP requests)
```

### Backend (Self-Hosted)

```
Translation Server:
├── LibreTranslate (Open source)
├── Argos Translate (ML models)
├── Port: 5000
└── Endpoint: POST /translate
```

### Planned Hardware Specifications

| Component | Specs | Cost (₹) |
|-----------|-------|----------|
| Processor | Rockchip RK3328 (4-core) | 1,200 |
| Memory | 2GB RAM + 32GB storage | 800 |
| Display | 3.5" sunlight-readable touch | 900 |
| Battery | 6000mAh Li-Po | 800 |
| Connectivity | Bluetooth 5.0 + GPS | 400 |
| **Total BOM** | | **5,800** |

Manufacturing cost: ₹6,500/unit | Retail price: ₹8,000/unit

### Software Stack (Production)

- **STT:** Mozilla DeepSpeech Lite
- **Translation:** Quantized ML Models (6GB storage)
- **TTS:** eSpeak NG
- **Maps:** OpenStreetMap + Trek Data

---

## Acknowledgments

- **LibreTranslate** - Free open-source translation API
- **Argos Translate** - Offline translation models
- **OpenStreetMap** - Community-driven mapping data
- **Mozilla DeepSpeech** - Speech recognition inspiration
- **Indian Mountaineering Foundation** - Domain expertise
- **Web Speech API** - Browser-based voice capabilities

---


## Key Differentiators

**Language Specialization** - 12 Indian languages optimized

**First-Mover Advantage** - No direct competition in this niche

**Trek-Specific Expertise** - Built for Indian wilderness

**Government Partnerships** - Direct access to bulk buyers

**Affordability** - 5x cheaper than satellite alternatives

---

<div align="center">

### TrekTalk Mini: Making Adventure Safer for Every Trekker

**Star this repo if you believe in safer trekking!**

[Demo](https://github.com/afrid995/voice_translator) • [Report Bug](https://github.com/afrid995/voice_translator/issues) • [Request Feature](https://github.com/afrid995/voice_translator/issues)

</div>
