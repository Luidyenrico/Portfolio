import sys
import re

with open(r'c:\Users\T-Gamer\Desktop\Portfolio\assets\index1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace About Section
about_pattern = re.compile(r'(<section id="about" class="section-padding border-b-grid relative">)(.*?)(?=</section>)', re.DOTALL)
new_about = r"""
            <div class="flex justify-between items-center ds-label mb-12">
                <span>(*05)</span><span>About</span>
            </div>
            
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 reveal items-center">
                <div class="lg:col-span-8 max-w-4xl">
                    <h2 class="text-4xl md:text-5xl lg:text-6xl font-heading leading-tight mb-8">
                        Crafting <span class="text-stroke text-transparent-stroke">technological experiences</span> that fuse precision engineering with stunning aesthetics.
                    </h2>
                    <p class="text-lg md:text-xl font-light leading-relaxed font-body" style="color:var(--text-secondary)">
                        I believe that enterprise software doesn't have to be brutalist. By bringing design systems thinking to data engineering and AI development, I build architectures that are not just highly performant and scalable, but intuitive and beautiful.
                    </p>
                </div>
                
                <div class="lg:col-span-4 flex justify-center lg:justify-end">
                    <!-- Abstract Decorative Element from design_system_main -->
                    <div class="relative w-64 h-64 lg:w-80 lg:h-80 cursor-hover-target">
                        <div class="absolute inset-0 rounded-full animate-[spin_40s_linear_infinite]" style="border:1px solid var(--border-color)"></div>
                        <div class="absolute inset-4 border-dashed rounded-full animate-[spin_30s_linear_infinite_reverse]" style="border:1px solid var(--border-color)"></div>
                        <div class="absolute inset-1/4 glass-panel rounded-full flex flex-col items-center justify-center backdrop-blur-xl">
                            <div class="text-3xl font-heading font-medium text-current">100%</div>
                            <div class="text-[10px] font-mono uppercase tracking-widest mt-1" style="color:var(--text-secondary)">Driven</div>
                        </div>
                    </div>
                </div>
            </div>
"""
html = about_pattern.sub(r'\1' + new_about, html)

# Replace Contact Section
contact_pattern = re.compile(r'(<section id="contact" class="section-padding relative">)(.*?)(?=</section>)', re.DOTALL)
new_contact = r"""
            <div class="flex justify-between items-center ds-label mb-12">
                <span>(*06)</span><span>Contact</span>
            </div>
            
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 reveal">
                <div>
                    <h2 class="text-4xl md:text-5xl font-heading mb-6">Let's build<br />something <span style="color:var(--accent-blue)">extraordinary.</span></h2>
                    <p class="text-lg mb-8" style="color:var(--text-secondary)">Available for freelance opportunities, AI infrastructure consulting, and design system engineering.</p>
                    
                    <div class="flex flex-col gap-4 font-mono text-sm">
                        <a href="mailto:hello@portfolio.com" class="hover:underline transition-all hover:text-[var(--accent-blue)] w-fit flex items-center gap-2">
                           <i data-lucide="mail" class="w-4 h-4"></i> hello@jane.dev
                        </a>
                        <a href="#" class="hover:underline transition-all hover:text-[var(--accent-blue)] w-fit flex items-center gap-2">
                           <i data-lucide="linkedin" class="w-4 h-4"></i> LinkedIn
                        </a>
                        <a href="#" class="hover:underline transition-all hover:text-[var(--accent-blue)] w-fit flex items-center gap-2">
                           <i data-lucide="github" class="w-4 h-4"></i> GitHub
                        </a>
                    </div>
                </div>
                
                <div class="glass-panel p-8 max-w-xl w-full justify-self-end">
                    <form class="flex flex-col gap-6" onsubmit="event.preventDefault()">
                        <div class="flex flex-col gap-2 relative">
                            <label class="text-xs font-mono" style="color:var(--text-secondary)">Name</label>
                            <div class="relative group">
                                <i data-lucide="user" class="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 transition-colors" style="color:var(--text-secondary)"></i>
                                <input type="text" placeholder="John Doe" class="w-full py-3 pl-12 pr-4 rounded-lg text-sm transition-all focus:outline-none" style="background:transparent;border:1px solid var(--border-color);color:var(--text-primary);" onfocus="this.style.borderColor=getComputedStyle(document.documentElement).getPropertyValue('--text-primary')" onblur="this.style.borderColor=getComputedStyle(document.documentElement).getPropertyValue('--border-color')">
                            </div>
                        </div>
                        
                        <div class="flex flex-col gap-2 relative">
                            <label class="text-xs font-mono" style="color:var(--text-secondary)">Email Address</label>
                            <div class="relative group">
                                <i data-lucide="mail" class="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 transition-colors" style="color:var(--text-secondary)"></i>
                                <input type="email" placeholder="hello@portfolio.ai" class="w-full py-3 pl-12 pr-4 rounded-lg text-sm transition-all focus:outline-none" style="background:transparent;border:1px solid var(--border-color);color:var(--text-primary);" onfocus="this.style.borderColor=getComputedStyle(document.documentElement).getPropertyValue('--text-primary')" onblur="this.style.borderColor=getComputedStyle(document.documentElement).getPropertyValue('--border-color')">
                            </div>
                        </div>
                        
                        <div class="flex flex-col gap-2 relative">
                            <label class="text-xs font-mono" style="color:var(--text-secondary)">Message</label>
                            <textarea placeholder="How can I help you?" rows="4" class="w-full py-3 px-4 rounded-lg text-sm transition-all focus:outline-none resize-none" style="background:transparent;border:1px solid var(--border-color);color:var(--text-primary);" onfocus="this.style.borderColor=getComputedStyle(document.documentElement).getPropertyValue('--text-primary')" onblur="this.style.borderColor=getComputedStyle(document.documentElement).getPropertyValue('--border-color')"></textarea>
                        </div>
                        
                        <button class="w-full py-3 rounded-lg font-medium text-sm flex items-center justify-center gap-2 group transition-all hover:scale-[1.02]" style="background:var(--text-primary);color:var(--bg-primary)">
                            <span>Send Message</span>
                            <i data-lucide="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1"></i>
                        </button>
                    </form>
                </div>
            </div>
"""
html = contact_pattern.sub(r'\1' + new_contact, html)

# Add Footer before closing main
footer = r"""
        <!-- ═══════════════════════════════════════
         FOOTER
         ═══════════════════════════════════════ -->
        <footer class="section-padding border-t w-full mt-24" style="border-color:var(--border-color)">
            <div class="flex flex-col md:flex-row justify-between items-center gap-6">
                <div class="flex items-center gap-2">
                    <iconify-icon icon="solar:atom-bold-duotone" class="text-xl" style="color:var(--accent-blue)"></iconify-icon>
                    <span class="font-heading font-semibold tracking-tight">DS.SYSTEM</span>
                </div>
                <div class="text-xs font-mono opacity-60">
                    &copy; 2025 Jane Doe. All systems nominal.
                </div>
            </div>
        </footer>
"""
html = html.replace('</main>', footer + '\n</main>')

# Fix the navigation links which refer to non-existent translations
auth_replace_js = r'''                hero_cta1: "Explore System", hero_cta2: "View Portfolio",'''
new_js = r'''                hero_cta1: "Explore System", hero_cta2: "View Portfolio",
                nav_projects: "Projects", nav_ai: "AI & Automation", nav_dashboards: "Dashboards", nav_about: "About", nav_contact: "Contact",'''
html = html.replace(auth_replace_js, new_js)

pt_js_old = r'''                hero_cta1: "Explorar Sistema", hero_cta2: "Ver Portf\u00f3lio",'''
pt_js_new = r'''                hero_cta1: "Explorar Sistema", hero_cta2: "Ver Portf\u00f3lio",
                nav_projects: "Projetos", nav_ai: "IA e Automa\u00e7\u00e3o", nav_dashboards: "Dashboards", nav_about: "Sobre", nav_contact: "Contato",'''
html = html.replace(pt_js_old, pt_js_new)

# Update the Nav Links completely with translation tags, as well as fixing the ones I previously put that didn't have data-i18n.
old_nav = """        <div class="nav-links hidden md:flex">
            <a href="#hero" class="nav-link">Hero</a>
            <a href="#projects" class="nav-link">Tipo</a>
            <a href="#ai-automation" class="nav-link">Cores</a>
            <a href="#dashboards" class="nav-link">Componentes</a>
            <a href="#about" class="nav-link">Ícones</a>
            <a href="#contact" class="nav-link">Movimento</a>
        </div>"""

new_nav = """        <div class="nav-links hidden md:flex">
            <a href="#hero" class="nav-link" data-i18n="nav_hero">Hero</a>
            <a href="#projects" class="nav-link" data-i18n="nav_projects">Projects</a>
            <a href="#ai-automation" class="nav-link" data-i18n="nav_ai">AI</a>
            <a href="#dashboards" class="nav-link" data-i18n="nav_dashboards">Dashboards</a>
            <a href="#about" class="nav-link" data-i18n="nav_about">About</a>
            <a href="#contact" class="nav-link" data-i18n="nav_contact">Contact</a>
        </div>"""
html = html.replace(old_nav, new_nav)


with open(r'c:\Users\T-Gamer\Desktop\Portfolio\assets\index1.html', 'w', encoding='utf-8') as f:
    f.write(html)
