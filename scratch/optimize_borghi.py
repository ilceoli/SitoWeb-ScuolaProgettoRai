import os

directory = r"c:\Users\ilceo\Desktop\GitHub\SitoWeb-ScuolaProgettoRai\assets\borghi"

override_css = """
        /* ==========================================================================
           OTTIMIZZAZIONE MOBILE E TABLET (ANDROID, IOS, IPAD)
           ========================================================================== */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column !important;
                gap: 15px !important;
                text-align: center !important;
                padding: 16px 0 !important;
            }
            .logo {
                flex-direction: column !important;
                align-items: center !important;
                text-align: center !important;
                gap: 6px !important;
            }
            .logo h1 {
                font-size: 1.15rem !important;
            }
            .logo span {
                font-size: 0.65rem !important;
                text-align: center !important;
            }
            .back-link {
                width: 100% !important;
                display: flex !important;
                justify-content: center !important;
                margin-top: 5px !important;
            }
            .back-link a {
                padding: 8px 24px !important;
                font-size: 0.85rem !important;
            }
            .content-section {
                display: flex !important;
                flex-direction: column !important;
                gap: 30px !important;
                direction: ltr !important;
            }
            .content-text {
                order: 1 !important;
                padding: 0 !important;
                text-align: justify !important;
            }
            .content-image {
                order: 2 !important;
                width: 100% !important;
                height: 280px !important;
            }
            .hero-borgo {
                min-height: 280px !important;
                height: 45vh !important;
            }
            .hero-borgo h2 {
                font-size: 2.2rem !important;
            }
            .hero-borgo p {
                font-size: 1.05rem !important;
            }
            .section-title {
                font-size: 2rem !important;
            }
            .info-grid {
                grid-template-columns: repeat(2, 1fr) !important;
                gap: 16px !important;
            }
            .tradizioni-grid {
                grid-template-columns: repeat(2, 1fr) !important;
                gap: 20px !important;
            }
        }

        @media (max-width: 480px) {
            .logo h1 {
                font-size: 0.95rem !important;
                white-space: normal !important;
            }
            .logo span {
                font-size: 0.6rem !important;
            }
            .logo img {
                height: 32px !important;
            }
            .info-grid {
                grid-template-columns: 1fr !important;
            }
            .tradizioni-grid {
                grid-template-columns: 1fr !important;
            }
            .gallery {
                grid-template-columns: 1fr !important;
                gap: 12px !important;
            }
            .gallery-item {
                height: 180px !important;
            }
            .hero-borgo {
                min-height: 220px !important;
                height: 35vh !important;
            }
            .hero-borgo h2 {
                font-size: 1.8rem !important;
            }
            .hero-borgo p {
                font-size: 0.9rem !important;
                line-height: 1.5 !important;
            }
            .section-title {
                font-size: 1.6rem !important;
            }
        }
    </style>
"""

count = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "OTTIMIZZAZIONE MOBILE E TABLET (ANDROID, IOS, IPAD)" in content:
                print(f"Skipping {file} (already optimized)")
                continue
                
            if "</style>" in content:
                # Split from right to replace the style block's closing tag
                parts = content.rsplit("</style>", 1)
                new_content = override_css.join(parts)
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Optimized styles in {file}")
                count += 1
            else:
                print(f"Warning: No </style> found in {file}")

print(f"Finished! Successfully optimized {count} HTML files.")
