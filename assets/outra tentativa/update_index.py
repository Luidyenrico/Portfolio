import sys
import re

with open(r'c:\Users\T-Gamer\Desktop\Portfolio\assets\index1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Nav links
old_nav = r"""        <div class="nav-links hidden md:flex">
            <a href="#hero" class="nav-link" data-i18n="nav_hero">Hero</a>
            <a href="#typography" class="nav-link" data-i18n="nav_type">Type</a>
            <a href="#colors" class="nav-link" data-i18n="nav_colors">Colors</a>
            <a href="#components" class="nav-link" data-i18n="nav_comp">Components</a>
            <a href="#icons" class="nav-link" data-i18n="nav_icons">Icons</a>
            <a href="#motion" class="nav-link" data-i18n="nav_motion">Motion</a>
            <a href="#theme-toggle" class="nav-link" data-i18n="nav_theme">Theme</a>
        </div>"""

new_nav = """        <div class="nav-links hidden md:flex">
            <a href="#hero" class="nav-link">Hero</a>
            <a href="#projects" class="nav-link">Tipo</a>
            <a href="#ai-automation" class="nav-link">Cores</a>
            <a href="#dashboards" class="nav-link">Componentes</a>
            <a href="#about" class="nav-link">Ícones</a>
            <a href="#contact" class="nav-link">Movimento</a>
        </div>"""
if old_nav in html:
    html = html.replace(old_nav, new_nav)
else:
    print("Could not find old_nav")

# Remove sections from Typography to Theme Toggle
start_marker = r'<!-- ═══════════════════════════════════════\s+02. TYPOGRAPHY\s+═══════════════════════════════════════ -->'
end_marker = r'</main>'

pattern = re.compile(f"{start_marker}.*?(?=</main>)", re.DOTALL)
if pattern.search(html):
    replacement_sections = """<!-- ═══════════════════════════════════════
         02. PROJECTS
         ═══════════════════════════════════════ -->
        <section id="projects" class="section-padding border-b-grid relative">
            <div class="flex justify-between items-center ds-label mb-12">
                <span>(*02)</span><span>Projects</span>
            </div>
            <!-- Glass Cards injected via JS or left as containers -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 reveal">
                <div class="glass-panel p-8 group relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-[var(--accent-glow)] rounded-full blur-3xl -translate-y-1/2 translate-x-1/2 group-hover:scale-150 transition-transform duration-700"></div>
                    <div class="relative z-10">
                        <div class="w-12 h-12 rounded-full bg-[var(--bg-primary)] border border-[var(--border-color)] flex items-center justify-center mb-6">
                            <i data-lucide="cpu" class="w-6 h-6 text-[var(--text-primary)]"></i>
                        </div>
                        <h4 class="text-xl font-heading mb-3">Project Alpha</h4>
                        <p class="text-[var(--text-secondary)] mb-6 text-sm">Advanced ML pipeline development and deployment using modern data architecture.</p>
                        <a href="#" class="inline-flex items-center gap-2 text-sm font-medium hover:text-[var(--accent-color)] transition-colors">
                            <span>Explore Module</span><i data-lucide="chevron-right" class="w-4 h-4"></i>
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- ═══════════════════════════════════════
         03. AI & AUTOMATION
         ═══════════════════════════════════════ -->
        <section id="ai-automation" class="section-padding border-b-grid relative">
            <div class="flex justify-between items-center ds-label mb-12">
                <span>(*03)</span><span>AI & Automation</span>
            </div>
            <div class="glass-panel p-8 reveal">
                <h3 class="text-2xl font-heading mb-4">Intelligent Systems Architecture</h3>
                <p class="text-[var(--text-secondary)] font-body max-w-2xl leading-relaxed">
                   Designing robust, scalable AI architectures that seamlessly integrate into existing workflows, ensuring ultra-low latency and high reliability.
                </p>
            </div>
        </section>

        <!-- ═══════════════════════════════════════
         04. DASHBOARDS
         ═══════════════════════════════════════ -->
        <section id="dashboards" class="section-padding border-b-grid relative">
            <div class="flex justify-between items-center ds-label mb-12">
                <span>(*04)</span><span>Dashboards</span>
            </div>
            <div class="glass-panel p-8 reveal">
                <!-- Metric Panel -->
                <div class="border border-[var(--border-color)] bg-[var(--bg-secondary)] p-8 relative overflow-hidden group">
                    <div class="flex justify-between items-start mb-8">
                        <span class="text-xs font-mono text-[var(--text-secondary)] tracking-widest">[ METRICS ]</span>
                    </div>
                    <h4 class="text-2xl font-heading mb-2 uppercase tracking-wide">Data Analytics</h4>
                    <div class="h-px w-full bg-gradient-to-r from-[var(--border-color)] to-transparent my-4"></div>
                </div>
            </div>
        </section>

        <!-- ═══════════════════════════════════════
         05. ABOUT
         ═══════════════════════════════════════ -->
        <section id="about" class="section-padding border-b-grid relative">
            <div class="flex justify-between items-center ds-label mb-12">
                <span>(*05)</span><span>About</span>
            </div>
             <div class="max-w-4xl reveal">
                <h2 class="text-4xl md:text-5xl font-heading leading-tight mb-8">
                    Crafting <span class="text-stroke">technological experiences</span> that fuse precision engineering with stunning aesthetics.
                </h2>
            </div>
        </section>

        <!-- ═══════════════════════════════════════
         06. CONTACT
         ═══════════════════════════════════════ -->
        <section id="contact" class="section-padding relative">
            <div class="flex justify-between items-center ds-label mb-12">
                <span>(*06)</span><span>Contact</span>
            </div>
            <div class="glass-panel p-8 reveal max-w-2xl">
                <div class="flex flex-col gap-6">
                    <div class="flex flex-col gap-2 relative">
                        <label class="text-xs font-mono text-[var(--text-secondary)]">Let's connect</label>
                        <div class="relative group">
                            <i data-lucide="mail" class="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-[var(--text-secondary)]"></i>
                            <input type="email" class="w-full bg-transparent border border-[var(--border-color)] rounded-lg py-3 pl-12 pr-4 text-[var(--text-primary)] placeholder-[var(--text-secondary)] focus:outline-none transition-colors" placeholder="hello@portfolio.com">
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""
    html = pattern.sub(replacement_sections, html)
else:
    print("Could not find start_marker for sections removal.")


# Replace Hero Title + add Marquee
old_hero_title = r"""            <!-- Hero Title -->
            <h1 id="hero-title"
                style="font-size:clamp(3.5rem,8.5vw,11rem);line-height:0.85;letter-spacing:-0.03em;text-transform:uppercase;display:flex;flex-wrap:wrap;align-items:center;gap:0.25em;position:relative;z-index:10;"
                class="font-heading">

                <!-- "Design" — transparent stroke + flicker -->
                <span class="text-reveal-wrapper">
                    <span class="text-reveal-content delay-300 flicker-word text-stroke font-heading"
                        style="display:block">Design</span>
                </span>

                <!-- Asterisk accent -->
                <span class="text-reveal-wrapper delay-200">
                    <iconify-icon icon="solar:asterisk-linear" class="text-reveal-content delay-200"
                        style="display:block;font-size:clamp(2.5rem,5vw,7rem);color:var(--accent-blue)"></iconify-icon>
                </span>

                <!-- "System" — solid, appears first -->
                <span class="text-reveal-wrapper">
                    <span class="text-reveal-content delay-100 font-heading" style="display:block">System</span>
                </span>
            </h1>

            <!-- Hero sub-grid -->
            <div class="mt-16 grid grid-cols-1 md:grid-cols-12 gap-8 relative z-10">
                <div class="md:col-span-4 border-t-grid pt-4">
                    <span class="ds-label" data-i18n="hero_status">[ Systems Online ]</span>
                    <!-- Animated status indicator -->
                    <div class="flex items-center gap-2 mt-4">
                        <span class="relative flex h-2 w-2">
                            <span class="animate-ping absolute inline-flex h-full w-full rounded-full opacity-75"
                                style="background:var(--accent-blue)"></span>
                            <span class="relative inline-flex rounded-full h-2 w-2"
                                style="background:var(--accent-blue)"></span>
                        </span>
                        <span class="text-xs font-mono" style="color:var(--text-secondary)" data-i18n="hero_online">Data
                            / AI / Automation</span>
                    </div>
                </div>
                <div class="md:col-span-8 text-base md:text-lg leading-relaxed max-w-3xl font-body"
                    style="color:var(--text-secondary)">
                    <span data-i18n="hero_desc">This document is the canonical pattern library — cataloguing typography,
                        color, interaction models, and component architecture that form the visual language of a modern
                        data and AI portfolio.</span>
                </div>
            </div>"""

new_hero_title = """            <!-- Hero Title -->
            <h1 id="hero-title"
                style="font-size:clamp(3.5rem,8.5vw,11rem);line-height:0.85;letter-spacing:-0.03em;text-transform:uppercase;display:flex;flex-wrap:wrap;align-items:center;gap:0.25em;position:relative;z-index:10;"
                class="font-heading">

                <span class="text-reveal-wrapper">
                    <span class="text-reveal-content delay-100 font-heading" style="display:block">Jane Doe</span>
                </span>
            </h1>

            <!-- Hero sub-grid -->
            <div class="mt-16 grid grid-cols-1 md:grid-cols-12 gap-8 relative z-10">
                <div class="md:col-span-4 border-t-grid pt-4">
                    <span class="ds-label">[ Data • AI • Automation ]</span>
                    <div class="flex items-center gap-2 mt-4">
                        <span class="relative flex h-2 w-2">
                            <span class="animate-ping absolute inline-flex h-full w-full rounded-full opacity-75"
                                style="background:var(--accent-blue)"></span>
                            <span class="relative inline-flex rounded-full h-2 w-2"
                                style="background:var(--accent-blue)"></span>
                        </span>
                        <span class="text-xs font-mono" style="color:var(--text-secondary)">Available for work</span>
                    </div>
                </div>
                <div class="md:col-span-8 text-base md:text-lg leading-relaxed max-w-3xl font-body"
                    style="color:var(--text-secondary)">
                    <span class="text-reveal-wrapper">
                        <span class="text-reveal-content delay-300 inline-block font-light">A technical professional specializing in data intelligence, AI models, and scalable automation systems crafting fluid, premium digital experiences.</span>
                    </span>
                </div>
            </div>

            <!-- Marquee Divider -->
            <div class="w-full mt-24 py-10 border-y relative overflow-hidden reveal glass-panel"
                style="border-color:var(--border-color);background:var(--bg-glass);backdrop-filter:blur(8px)">
                <div class="marquee-container">
                    <div class="marquee-content font-heading uppercase tracking-tighter opacity-30"
                        style="font-size:clamp(2rem,4vw,4rem)">
                        <span class="mx-8">AI</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">INTELLIGENCE</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">AUTOMATION</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">SYSTEMS</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">DATA</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">ANALYTICS</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">PYTHON</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                    </div>
                    <!-- Duplicate for infinite scroll -->
                    <div class="marquee-content font-heading uppercase tracking-tighter opacity-30"
                        style="font-size:clamp(2rem,4vw,4rem)">
                        <span class="mx-8">AI</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">INTELLIGENCE</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">AUTOMATION</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">SYSTEMS</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">DATA</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">ANALYTICS</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                        <span class="mx-8">PYTHON</span>
                        <iconify-icon icon="solar:star-fall-bold-duotone" class="text-4xl self-center" style="color:var(--accent-blue)"></iconify-icon>
                    </div>
                </div>
            </div>"""

if old_hero_title in html:
    html = html.replace(old_hero_title, new_hero_title)
else:
    print("Could not find old_hero_title")

with open(r'c:\Users\T-Gamer\Desktop\Portfolio\assets\index1.html', 'w', encoding='utf-8') as f:
    f.write(html)
