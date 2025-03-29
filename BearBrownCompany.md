# 🎧 BearBrownCompany Music Website

Welcome to the official repository for **BearBrownCompany** — a music production platform where artists can upload, showcase, and explore original music. Built using **React**, **Tailwind CSS**, and UI components generated with **[V0.dev by Vercel](https://v0.dev)**.

> 🔥 Raw. Real. Resonant.

---

## 🧠 How Vercel V0 Works

[V0.dev](https://v0.dev) is an AI-powered UI generation tool by Vercel that turns natural language prompts into production-ready **React components** styled with **Tailwind CSS**.

### Key Features:
- ✨ **Prompt-to-code UI generation**: Describe what you want in plain English.
- 💅 **Uses ShadCN/UI components**: Elegant, accessible, and customizable.
- 🎨 **Tailwind CSS styling**: Clean, utility-based design.
- 🧱 **Component-based output**: Easily copy, paste, and integrate.
- 🔁 **Editable canvas**: Modify components visually or in code.

For this project, we used V0.dev to generate layout and UI for each page, maintaining a consistent dark aesthetic and component structure.

---

## 🧩 Tech Stack

| Layer             | Tech Used                      |
|------------------|--------------------------------|
| 🧠 UI Generation | [V0.dev](https://v0.dev)        |
| ⚛️ Frontend       | React                          |
| 🎨 Styling        | Tailwind CSS                   |
| 🧱 Components     | [shadcn/ui](https://ui.shadcn.com/) |
| 📦 Routing        | (Optional) Next.js for pages   |
| 💾 Backend        | Not included (frontend only)   |

---

## 📁 Project Structure

This website is designed as a multi-page React app with modular components and consistent layout.

```bash
/pages
  ├── index.tsx        # Homepage
  ├── upload.tsx       # Track Upload
  ├── tracks.tsx       # Track Gallery
  ├── about.tsx        # About
  ├── contact.tsx      # Contact
  └── admin.tsx        # Admin Dashboard (optional)
  
/components
  ├── Layout.tsx       # Global layout wrapper
  ├── Navbar.tsx
  ├── Footer.tsx
  ├── TrackCard.tsx
  └── UploadForm.tsx
```

---

## 💬 V0 Prompts Used

Each section of the website was generated using prompts in [V0.dev](https://v0.dev). Below are the exact prompts used to create the site.

### 1. 🧱 Global Layout
```
Create a global layout for "BearBrownCompany", a music production website. Include a dark-themed navbar with the logo, navigation links (Home, Upload, Tracks, About, Contact), and a sticky header. Add a footer with copyright info and social links.
```

### 2. 🏠 Homepage
```
Design a homepage for BearBrownCompany with a full-screen hero section, tagline "Raw. Real. Resonant.", top featured tracks, about blurb, and a call-to-action to upload or explore tracks. Match layout and style with the global layout.
```

### 3. 📀 Track Gallery
```
Create a public-facing track gallery page that lists music uploaded by artists. Each card should have album art, title, artist, genre, and a play button. Add a search bar and genre filter. Match BearBrownCompany's dark branding.
```

### 4. ⬆️ Upload Page
```
Design a track upload form for BearBrownCompany. Fields: Track Title, Genre (dropdown), Description, Upload File (MP3/WAV). After upload, show the uploaded tracks in a list. Styled to match rest of site. Use same global layout.
```

### 5. 🧑‍🎤 About Page
```
Create an About page for BearBrownCompany. Include a mission statement, founders' bios, and testimonials from artists. Use gritty, modern design that fits the music brand.
```

### 6. 📫 Contact Page
```
Design a contact page for BearBrownCompany with a form (name, email, message), social media icons, and contact info. Keep consistent style and layout.
```

### 7. 🛠️ Admin Dashboard (Optional)
```
Design an admin dashboard for BearBrownCompany to manage uploaded tracks. Include navigation on the left, a table showing track title, upload date, genre, and actions like edit/delete. Use a minimal, professional style.
```

---

## 📌 How to Use V0.dev Efficiently

- 🧱 **Start with the layout**: Navbar + Footer ensures consistency across pages.
- ✍️ **Be descriptive in prompts**: Mention brand name, tone (dark, modern, etc.), and functionality.
- ♻️ **Re-use components**: Especially layout, buttons, and cards.
- 🧠 **Use terms like**: “Use same layout”, “match previous style” to enforce UI consistency.
- 🧩 **Organize output cleanly**: Paste each component into your app with proper routing.

---

## 🐻 Made with love by BearBrownCompany
```

