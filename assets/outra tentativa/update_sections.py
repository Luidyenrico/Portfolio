import sys
import re

with open(r'c:\Users\T-Gamer\Desktop\Portfolio\assets\index1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Projects Section inner content
projects_pattern = re.compile(r'(<section id="projects" class="section-padding border-b-grid relative">)(.*?)(?=</section>)', re.DOTALL)

new_projects = r"""
            <div class="flex justify-between items-center ds-label mb-12">
                <span>(*02)</span><span>Projects</span>
            </div>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 reveal">
                <!-- Project 1 -->
                <div class="glass-panel p-8 group relative overflow-hidden flex flex-col h-full cursor-hover-target">
                    <div class="absolute top-0 right-0 w-48 h-48 rounded-full blur-[64px] -translate-y-1/2 translate-x-1/2 group-hover:scale-150 transition-transform duration-700 pointer-events-none" style="background:var(--accent-blue);opacity:0.25"></div>
                    <div class="relative z-10 flex-1 flex flex-col">
                        <div class="w-12 h-12 mb-6 flex items-center justify-center rounded-lg" style="background:var(--bg-primary);border:1px solid var(--border-color)">
                            <i data-lucide="database" class="w-6 h-6" style="color:var(--text-primary)"></i>
                        </div>
                        <h4 class="text-2xl font-heading mb-3 font-medium">Data Lake Architecture</h4>
                        <p class="text-base mb-6 font-body leading-relaxed flex-1" style="color:var(--text-secondary)">
                            A hyper-scalable data lake implementation handling 50TB+ of daily streaming data, optimized for milliseconds latency querying and ML training pipelines.
                        </p>
                        <div class="flex flex-wrap gap-2 mb-8">
                            <span class="text-xs font-mono px-2 py-1 rounded" style="background:var(--bg-primary);border:1px solid var(--border-color);color:var(--text-secondary)">Kafka</span>
                            <span class="text-xs font-mono px-2 py-1 rounded" style="background:var(--bg-primary);border:1px solid var(--border-color);color:var(--text-secondary)">Spark</span>
                            <span class="text-xs font-mono px-2 py-1 rounded" style="background:var(--bg-primary);border:1px solid var(--border-color);color:var(--text-secondary)">AWS</span>
                        </div>
                        <a href="#" class="inline-flex items-center gap-2 text-sm font-medium transition-colors w-fit group/link" style="color:var(--text-primary)"
                            onmouseover="this.style.color=getComputedStyle(document.documentElement).getPropertyValue('--accent-blue')"
                            onmouseout="this.style.color=getComputedStyle(document.documentElement).getPropertyValue('--text-primary')">
                            <span>View Architecture</span>
                            <i data-lucide="arrow-right" class="w-4 h-4 transition-transform group-hover/link:translate-x-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Project 2 -->
                <div class="glass-panel p-8 group relative overflow-hidden flex flex-col h-full cursor-hover-target">
                    <div class="absolute top-0 right-0 w-48 h-48 rounded-full blur-[64px] -translate-y-1/2 translate-x-1/2 group-hover:scale-150 transition-transform duration-700 pointer-events-none" style="background:var(--accent-blue);opacity:0.25"></div>
                    <div class="relative z-10 flex-1 flex flex-col">
                        <div class="w-12 h-12 mb-6 flex items-center justify-center rounded-lg" style="background:var(--bg-primary);border:1px solid var(--border-color)">
                            <i data-lucide="cpu" class="w-6 h-6" style="color:var(--text-primary)"></i>
                        </div>
                        <h4 class="text-2xl font-heading mb-3 font-medium">Neural Trading Engine</h4>
                        <p class="text-base mb-6 font-body leading-relaxed flex-1" style="color:var(--text-secondary)">
                            Autonomous trading system leveraging deep reinforcement learning to execute high-frequency trades across decentralized exchanges with 99.99% uptime.
                        </p>
                        <div class="flex flex-wrap gap-2 mb-8">
                            <span class="text-xs font-mono px-2 py-1 rounded" style="background:var(--bg-primary);border:1px solid var(--border-color);color:var(--text-secondary)">PyTorch</span>
                            <span class="text-xs font-mono px-2 py-1 rounded" style="background:var(--bg-primary);border:1px solid var(--border-color);color:var(--text-secondary)">Rust</span>
                            <span class="text-xs font-mono px-2 py-1 rounded" style="background:var(--bg-primary);border:1px solid var(--border-color);color:var(--text-secondary)">Web3</span>
                        </div>
                        <a href="#" class="inline-flex items-center gap-2 text-sm font-medium transition-colors w-fit group/link" style="color:var(--text-primary)"
                            onmouseover="this.style.color=getComputedStyle(document.documentElement).getPropertyValue('--accent-blue')"
                            onmouseout="this.style.color=getComputedStyle(document.documentElement).getPropertyValue('--text-primary')">
                            <span>View Architecture</span>
                            <i data-lucide="arrow-right" class="w-4 h-4 transition-transform group-hover/link:translate-x-1"></i>
                        </a>
                    </div>
                </div>
            </div>
"""

html = projects_pattern.sub(r'\1' + new_projects, html)

# Replace AI & Automation Section
ai_pattern = re.compile(r'(<section id="ai-automation" class="section-padding border-b-grid relative">)(.*?)(?=</section>)', re.DOTALL)
new_ai = r"""
            <div class="flex justify-between items-center ds-label mb-12">
                <span>(*03)</span><span>AI & Automation</span>
            </div>
            
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 reveal">
                <div class="lg:col-span-7 flex flex-col justify-center">
                    <h3 class="text-3xl md:text-5xl font-heading mb-6 tracking-tight leading-tight">
                        Intelligent workflows <br />
                        <span class="text-stroke">running 24/7.</span>
                    </h3>
                    <p class="text-lg font-body max-w-xl leading-relaxed mb-8" style="color:var(--text-secondary)">
                       Designing robust, scalable AI architectures that seamlessly integrate into existing platforms. From NLP-powered concierges to fully autonomous ETL pipelines, prioritizing ultra-low latency and fault tolerance.
                    </p>
                    <div class="flex gap-12 font-mono text-sm">
                        <div class="flex flex-col gap-2">
                            <span class="text-3xl font-heading" style="color:var(--text-primary)">99.9%</span>
                            <span style="color:var(--text-secondary)">Uptime</span>
                        </div>
                        <div class="flex flex-col gap-2">
                            <span class="text-3xl font-heading" style="color:var(--text-primary)">5M+</span>
                            <span style="color:var(--text-secondary)">Tasks Auto</span>
                        </div>
                    </div>
                </div>

                <div class="lg:col-span-5 relative mt-12 lg:mt-0">
                    <!-- Terminal Card Component -->
                    <div class="p-8 relative overflow-hidden group w-full h-full min-h-[350px]"
                        style="border:1px solid var(--border-color);background:var(--bg-secondary)">
                        <div class="corner-accent" style="top:0;left:0;border-top:1px solid var(--text-primary);border-left:1px solid var(--text-primary)"></div>
                        <div class="corner-accent" style="top:0;right:0;border-top:1px solid var(--text-primary);border-right:1px solid var(--text-primary)"></div>
                        <div class="corner-accent" style="bottom:0;left:0;border-bottom:1px solid var(--text-primary);border-left:1px solid var(--text-primary)"></div>
                        <div class="corner-accent" style="bottom:0;right:0;border-bottom:1px solid var(--text-primary);border-right:1px solid var(--text-primary)"></div>
                        
                        <div class="flex justify-between items-start mb-8 relative z-10">
                            <span class="text-xs font-mono tracking-widest" style="color:var(--text-secondary)">[ SYS.AUTO ]</span>
                            <span class="relative flex h-3 w-3">
                                <span class="animate-ping absolute inline-flex h-full w-full rounded-full opacity-75" style="background:var(--accent-blue)"></span>
                                <span class="relative inline-flex rounded-full h-3 w-3" style="background:#22c55e"></span>
                            </span>
                        </div>
                        
                        <h4 class="text-2xl font-heading mb-2 uppercase tracking-wide relative z-10">Cron Node Omega</h4>
                        <div class="h-px w-full my-4 relative z-10" style="background:linear-gradient(to right,var(--border-color),transparent)"></div>
                        
                        <div class="font-mono text-xs space-y-2 mt-6 relative z-10" style="color:var(--text-secondary)">
                            <p class="mb-4">&gt; INITIALIZING AGENT SWARM...</p>
                            <div class="flex justify-between border-b pb-2" style="border-color:var(--border-color)">
                                <span>Task: NLP Extraction</span>
                                <span style="color:var(--text-primary)">Running</span>
                            </div>
                            <div class="flex justify-between border-b pb-2 pt-2" style="border-color:var(--border-color)">
                                <span>Task: Model Retraining</span>
                                <span style="color:#22c55e">Completed</span>
                            </div>
                            <div class="flex justify-between pt-2">
                                <span>Task: API Sync</span>
                                <span class="animate-pulse" style="color:var(--accent-blue)">Processing</span>
                            </div>
                            
                            <p class="mt-6" style="color:var(--text-primary)">&gt; SYSTEM STATUS: <span style="color:#22c55e">OPTIMAL</span></p>
                        </div>

                        <!-- Scanline effect -->
                        <div class="absolute inset-0 pointer-events-none opacity-20" style="background:linear-gradient(to bottom, transparent 50%, rgba(0,0,0,0.1) 51%);background-size:100% 4px;z-index:1"></div>
                    </div>
                </div>
            </div>
"""
html = ai_pattern.sub(r'\1' + new_ai, html)

# Replace Dashboards Section
dash_pattern = re.compile(r'(<section id="dashboards" class="section-padding border-b-grid relative">)(.*?)(?=</section>)', re.DOTALL)
new_dash = r"""
            <div class="flex justify-between items-center ds-label mb-12">
                <span>(*04)</span><span>Dashboards</span>
            </div>
            
            <div class="mb-12 reveal">
                <h2 class="text-3xl md:text-5xl font-heading tracking-tight mb-4">Actionable Analytics.</h2>
                <p class="text-lg" style="color:var(--text-secondary)">Bringing complex datasets to the surface with bespoke visualization interfaces.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 reveal">
                <!-- Metric Panel 1 -->
                <div class="glass-panel p-6 relative overflow-hidden group">
                    <div class="flex justify-between items-start mb-6">
                        <div class="w-10 h-10 rounded-full flex items-center justify-center" style="background:var(--bg-secondary);border:1px solid var(--border-color)">
                            <i data-lucide="activity" class="w-5 h-5 text-current"></i>
                        </div>
                        <span class="text-xs font-mono px-2 py-1 rounded" style="background:rgba(34,197,94,0.1);color:#22c55e">+14.5%</span>
                    </div>
                    <p class="text-sm font-mono mb-1" style="color:var(--text-secondary)">Stream Throughput</p>
                    <p class="text-3xl font-heading mb-4">42.8 GB/s</p>
                    <div class="w-full h-8 flex items-end gap-1 opacity-60">
                        <div class="w-full bg-current rounded-t-sm transition-all group-hover:h-8 h-3"></div>
                        <div class="w-full bg-current rounded-t-sm transition-all group-hover:h-5 h-5"></div>
                        <div class="w-full bg-current rounded-t-sm transition-all group-hover:h-2 h-7"></div>
                        <div class="w-full bg-current rounded-t-sm transition-all group-hover:h-6 h-4"></div>
                        <div class="w-full bg-current rounded-t-sm transition-all group-hover:h-8 h-8"></div>
                        <div class="w-full bg-current rounded-t-sm transition-all group-hover:h-4 h-6"></div>
                    </div>
                </div>

                <!-- Metric Panel 2 -->
                <div class="glass-panel p-6 relative overflow-hidden group" style="background:var(--text-primary);color:var(--bg-primary)">
                    <div class="absolute inset-0 opacity-10" style="background-image:radial-gradient(circle at 50% 0%, var(--bg-primary) 0%, transparent 70%)"></div>
                    <div class="flex justify-between items-start mb-6 relative z-10">
                        <div class="w-10 h-10 rounded-full flex items-center justify-center" style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2)">
                            <i data-lucide="layers" class="w-5 h-5 text-current"></i>
                        </div>
                        <span class="text-xs font-mono px-2 py-1 rounded bg-white text-black font-semibold">LIVE</span>
                    </div>
                    <p class="text-sm font-mono mb-1 relative z-10" style="color:var(--bg-secondary)">Active Pipelines</p>
                    <p class="text-3xl font-heading mb-4 relative z-10">1,204</p>
                    <p class="text-xs font-mono relative z-10 opacity-70">Processing 2.4M rows/min</p>
                </div>

                <div class="glass-panel p-6 relative flex flex-col justify-center items-center text-center cursor-pointer group hover:bg-transparent">
                     <div class="w-12 h-12 rounded-full mb-4 flex items-center justify-center transition-transform group-hover:scale-110 group-hover:rotate-12" style="background:transparent;border:1px dashed var(--text-primary)">
                         <i data-lucide="arrow-right" class="w-5 h-5"></i>
                     </div>
                     <h4 class="font-heading font-medium text-lg">View Use Cases</h4>
                     <p class="text-xs font-mono mt-2" style="color:var(--text-secondary)">Case Studies &rarr;</p>
                </div>
            </div>
"""
html = dash_pattern.sub(r'\1' + new_dash, html)

with open(r'c:\Users\T-Gamer\Desktop\Portfolio\assets\index1.html', 'w', encoding='utf-8') as f:
    f.write(html)
