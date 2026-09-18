"""
Inline SVG diagrams for the playbook PDF.
Each function returns a self-contained <svg>...</svg> string sized for A5.
Dark theme; teal (#4CE0D6) → violet (#7A5CFF) accent palette.
"""

# Common defs used by many diagrams
_DEFS = """
  <defs>
    <linearGradient id="grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#4CE0D6"/>
      <stop offset="1" stop-color="#7A5CFF"/>
    </linearGradient>
    <linearGradient id="gradSoft" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#4CE0D6" stop-opacity="0.18"/>
      <stop offset="1" stop-color="#7A5CFF" stop-opacity="0.18"/>
    </linearGradient>
    <linearGradient id="gradWarn" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F5C453"/>
      <stop offset="1" stop-color="#F58BB6"/>
    </linearGradient>
    <linearGradient id="gradGood" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#6EE7A2"/>
      <stop offset="1" stop-color="#4CE0D6"/>
    </linearGradient>
  </defs>
"""

_S = {
    "ink":       "#F0F4FF",
    "inkSoft":   "rgba(240,244,255,0.72)",
    "inkMute":   "rgba(240,244,255,0.55)",
    "line":      "rgba(140,170,255,0.28)",
    "lineSoft":  "rgba(140,170,255,0.14)",
    "card":      "rgba(20,34,78,0.55)",
    "teal":      "#4CE0D6",
    "violet":    "#7A5CFF",
    "amber":     "#F5C453",
    "pink":      "#F58BB6",
    "green":     "#6EE7A2",
    "blue":      "#7DA7FF",
    "red":       "#F58BB6",
}


def chatbot_vs_agent() -> str:
    s = _S
    return f"""
<figure class="pb-figure">
<svg viewBox="0 0 500 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Three types of AI: chatbot, assistant, agent">
{_DEFS}
  <!-- three columns -->
  <g font-family="Inter, sans-serif" fill="{s['ink']}">
    <!-- chatbot -->
    <g transform="translate(10,10)">
      <rect width="150" height="240" rx="10" fill="{s['card']}" stroke="{s['line']}"/>
      <text x="75" y="30" text-anchor="middle" font-size="11" font-weight="800" fill="{s['blue']}" letter-spacing="2">CHATBOT</text>
      <text x="75" y="50" text-anchor="middle" font-size="9" fill="{s['inkMute']}">Answers questions</text>
      <g transform="translate(60,72)" fill="none" stroke="{s['blue']}" stroke-width="1.5">
        <rect x="0" y="0" width="30" height="22" rx="4"/>
        <path d="M15 22 L18 30 L22 22"/>
        <circle cx="9" cy="11" r="1.5" fill="{s['blue']}" stroke="none"/>
        <circle cx="21" cy="11" r="1.5" fill="{s['blue']}" stroke="none"/>
      </g>
      <g font-size="8.5" fill="{s['inkSoft']}">
        <text x="14" y="130">✓ Text in, text out</text>
        <text x="14" y="146">✗ No file access</text>
        <text x="14" y="162">✗ No commands</text>
        <text x="14" y="178">✗ No testing</text>
      </g>
      <text x="75" y="215" text-anchor="middle" font-size="9" fill="{s['inkMute']}" font-style="italic">"Like a friend</text>
      <text x="75" y="228" text-anchor="middle" font-size="9" fill="{s['inkMute']}" font-style="italic">on the phone."</text>
    </g>
    <!-- assistant -->
    <g transform="translate(175,10)">
      <rect width="150" height="240" rx="10" fill="{s['card']}" stroke="{s['line']}"/>
      <text x="75" y="30" text-anchor="middle" font-size="11" font-weight="800" fill="{s['amber']}" letter-spacing="2">ASSISTANT</text>
      <text x="75" y="50" text-anchor="middle" font-size="9" fill="{s['inkMute']}">Suggests as you type</text>
      <g transform="translate(52,68)" fill="none" stroke="{s['amber']}" stroke-width="1.5">
        <rect x="0" y="0" width="46" height="32" rx="3"/>
        <line x1="4" y1="8" x2="30" y2="8"/>
        <line x1="4" y1="15" x2="42" y2="15"/>
        <line x1="4" y1="22" x2="26" y2="22"/>
        <rect x="4" y="26" width="24" height="3" fill="{s['amber']}" fill-opacity="0.35" stroke="none"/>
      </g>
      <g font-size="8.5" fill="{s['inkSoft']}">
        <text x="14" y="130">✓ Sees your file</text>
        <text x="14" y="146">✓ Autocompletes code</text>
        <text x="14" y="162">✗ Doesn't run code</text>
        <text x="14" y="178">✗ Doesn't edit files</text>
      </g>
      <text x="75" y="215" text-anchor="middle" font-size="9" fill="{s['inkMute']}" font-style="italic">"Like autocomplete</text>
      <text x="75" y="228" text-anchor="middle" font-size="9" fill="{s['inkMute']}" font-style="italic">with a brain."</text>
    </g>
    <!-- agent -->
    <g transform="translate(340,10)">
      <rect width="150" height="240" rx="10" fill="url(#gradSoft)" stroke="{s['teal']}" stroke-width="1.5"/>
      <text x="75" y="30" text-anchor="middle" font-size="11" font-weight="800" fill="{s['teal']}" letter-spacing="2">AGENT</text>
      <text x="75" y="50" text-anchor="middle" font-size="9" fill="{s['inkMute']}">Takes actions</text>
      <g transform="translate(50,66)" fill="none" stroke="{s['teal']}" stroke-width="1.5">
        <circle cx="25" cy="18" r="14"/>
        <path d="M25 4 L25 32 M11 18 L39 18 M15 8 L35 28 M35 8 L15 28" stroke-opacity="0.5"/>
        <circle cx="25" cy="18" r="4" fill="{s['teal']}" fill-opacity="0.4" stroke="none"/>
      </g>
      <g font-size="8.5" fill="{s['inkSoft']}">
        <text x="14" y="118">✓ Reads whole project</text>
        <text x="14" y="132">✓ Edits many files</text>
        <text x="14" y="146">✓ Runs commands</text>
        <text x="14" y="160">✓ Runs tests</text>
        <text x="14" y="174">✓ Fixes its own errors</text>
        <text x="14" y="188">⚠ Needs your rules</text>
      </g>
      <text x="75" y="215" text-anchor="middle" font-size="9" fill="{s['inkMute']}" font-style="italic">"Like a junior dev</text>
      <text x="75" y="228" text-anchor="middle" font-size="9" fill="{s['inkMute']}" font-style="italic">at your desk."</text>
    </g>
  </g>
</svg>
<figcaption>The three kinds of AI helpers you can talk to. The right-most one is the topic of this book.</figcaption>
</figure>
"""


def framework_flow() -> str:
    """The 8-stage flow. Fits on a full page."""
    s = _S
    stages = [
        ("01", "DEFINE",       "What is the job?",           s['teal']),
        ("02", "CONTEXT",      "What is this project?",      s['teal']),
        ("03", "INVESTIGATE",  "What's already there?",      s['teal']),
        ("04", "BOUNDARIES",   "What must not change?",      s['amber']),
        ("05", "EXECUTE",      "Small step. Look. Repeat.",  s['violet']),
        ("06", "VERIFY",       "Prove it works.",            s['violet']),
        ("07", "REVIEW",       "Read every change.",         s['pink']),
        ("08", "LEARN",        "Turn surprise into rule.",   s['green']),
    ]
    rows = ""
    for i, (n, name, desc, col) in enumerate(stages):
        y = 20 + i * 42
        rows += f"""
    <g transform="translate(0,{y})">
      <line x1="60" y1="20" x2="80" y2="20" stroke="{col}" stroke-width="2"/>
      <circle cx="42" cy="20" r="18" fill="{s['card']}" stroke="{col}" stroke-width="1.5"/>
      <text x="42" y="24" text-anchor="middle" font-size="10" font-weight="800" fill="{col}">{n}</text>
      <rect x="80" y="6" width="260" height="28" rx="6" fill="{s['card']}" stroke="{s['line']}"/>
      <text x="94" y="24" font-size="11" font-weight="800" fill="{s['ink']}">{name}</text>
      <text x="180" y="24" font-size="10" fill="{s['inkSoft']}">{desc}</text>
    </g>
"""
        if i < len(stages) - 1:
            rows += f"""
    <line x1="42" y1="{y+40}" x2="42" y2="{y+60}" stroke="{col}" stroke-width="2" stroke-dasharray="3 3" opacity="0.7"/>
    <polygon points="42,{y+62} 38,{y+56} 46,{y+56}" fill="{col}" opacity="0.9"/>
"""
    return f"""
<figure class="pb-figure pb-figure--full">
<svg viewBox="0 0 360 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Eight-stage workflow">
{_DEFS}
  <g font-family="Inter, sans-serif">
    {rows}
  </g>
</svg>
<figcaption>The eight stages. Skipping one is almost always why a task falls apart.</figcaption>
</figure>
"""


def blast_radius() -> str:
    s = _S
    return f"""
<figure class="pb-figure">
<svg viewBox="0 0 420 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Blast radius: how far a change can reach">
{_DEFS}
  <!-- concentric rings -->
  <g transform="translate(140,120)">
    <circle r="105" fill="none" stroke="{s['red']}" stroke-opacity="0.35" stroke-width="1" stroke-dasharray="3 3"/>
    <circle r="80"  fill="none" stroke="{s['amber']}" stroke-opacity="0.45" stroke-width="1" stroke-dasharray="3 3"/>
    <circle r="55"  fill="none" stroke="{s['teal']}" stroke-opacity="0.55" stroke-width="1" stroke-dasharray="3 3"/>
    <circle r="30"  fill="url(#gradSoft)" stroke="{s['teal']}" stroke-width="1.5"/>
    <text y="4" text-anchor="middle" font-size="10" font-weight="700" fill="{s['ink']}" font-family="Inter, sans-serif">the change</text>
  </g>
  <!-- labels -->
  <g font-family="Inter, sans-serif" font-size="9.5">
    <text x="260" y="60" fill="{s['red']}" font-weight="700">Payments</text>
    <text x="260" y="74" fill="{s['inkSoft']}">Real money moves.</text>
    <text x="260" y="98" fill="{s['red']}" font-weight="700">Authentication</text>
    <text x="260" y="112" fill="{s['inkSoft']}">Users get locked out.</text>
    <text x="260" y="136" fill="{s['amber']}" font-weight="700">Database schema</text>
    <text x="260" y="150" fill="{s['inkSoft']}">Every page that read it breaks.</text>
    <text x="260" y="174" fill="{s['teal']}" font-weight="700">Shared component</text>
    <text x="260" y="188" fill="{s['inkSoft']}">Other pages using it also change.</text>
    <text x="260" y="212" fill="{s['ink']}" font-weight="700">This one file</text>
    <text x="260" y="226" fill="{s['inkSoft']}">Only the thing you meant.</text>
  </g>
</svg>
<figcaption>Before you push the button, ask: how far can this reach if it goes wrong?</figcaption>
</figure>
"""


def investigate_pipeline() -> str:
    s = _S
    steps = [
        ("READ",       "Open the right files."),
        ("TRACE",      "Follow how they connect."),
        ("UNDERSTAND", "See what the code does now."),
        ("PLAN",       "Write the change in words."),
        ("EDIT",       "Now — and only now — change code."),
    ]
    boxes = ""
    for i, (name, desc) in enumerate(steps):
        x = 10 + i * 88
        boxes += f"""
    <g transform="translate({x},60)">
      <rect width="78" height="70" rx="8" fill="{s['card']}" stroke="{s['teal']}" stroke-opacity="0.6" stroke-width="1.5"/>
      <text x="39" y="26" text-anchor="middle" font-size="10" font-weight="800" fill="{s['teal']}">{name}</text>
      <foreignObject x="4" y="34" width="70" height="34">
        <div xmlns="http://www.w3.org/1999/xhtml" style="font: 8.5px Inter; color: rgba(240,244,255,0.72); text-align:center; line-height:1.3;">{desc}</div>
      </foreignObject>
    </g>
"""
        if i < len(steps) - 1:
            arrow_x = x + 78
            boxes += f"""
    <path d="M{arrow_x} 95 L{arrow_x+10} 95" stroke="{s['teal']}" stroke-width="1.5"/>
    <polygon points="{arrow_x+10},95 {arrow_x+6},92 {arrow_x+6},98" fill="{s['teal']}"/>
"""
    return f"""
<figure class="pb-figure">
<svg viewBox="0 0 460 160" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Investigate pipeline: read, trace, understand, plan, edit">
{_DEFS}
  <g font-family="Inter, sans-serif">
    <text x="10" y="30" font-size="11" fill="{s['inkMute']}" letter-spacing="3">LOOK BEFORE YOU LEAP</text>
    {boxes}
  </g>
</svg>
<figcaption>The five-step order every safe change follows. Edit is last.</figcaption>
</figure>
"""


def small_vs_big() -> str:
    s = _S
    return f"""
<figure class="pb-figure">
<svg viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Small change vs big change">
{_DEFS}
  <g font-family="Inter, sans-serif">
    <!-- big change (bad) -->
    <g transform="translate(10,10)">
      <rect width="230" height="200" rx="10" fill="{s['card']}" stroke="{s['red']}" stroke-opacity="0.5"/>
      <text x="115" y="26" text-anchor="middle" font-size="10" fill="{s['red']}" font-weight="800" letter-spacing="2">ONE BIG CHANGE</text>
      <g transform="translate(20,44)">
        <rect width="190" height="26" rx="4" fill="{s['red']}" fill-opacity="0.15" stroke="{s['red']}" stroke-opacity="0.4"/>
        <text x="10" y="17" font-size="9" fill="{s['ink']}">"Redesign the whole app"</text>
      </g>
      <g fill="{s['inkSoft']}" font-size="9">
        <text x="20" y="96">✗ Hard to read the diff</text>
        <text x="20" y="112">✗ Hard to test</text>
        <text x="20" y="128">✗ Hard to undo</text>
        <text x="20" y="144">✗ When it breaks — where?</text>
        <text x="20" y="160">✗ Never fully finished</text>
      </g>
      <text x="115" y="185" text-anchor="middle" font-size="9" fill="{s['red']}" font-weight="700">1 giant leap</text>
    </g>
    <!-- small changes (good) -->
    <g transform="translate(260,10)">
      <rect width="230" height="200" rx="10" fill="url(#gradSoft)" stroke="{s['green']}" stroke-width="1.5"/>
      <text x="115" y="26" text-anchor="middle" font-size="10" fill="{s['green']}" font-weight="800" letter-spacing="2">SMALL STEPS</text>
      <g transform="translate(20,44)" font-size="8.5" fill="{s['ink']}">
        <g>
          <rect width="190" height="22" rx="3" fill="{s['green']}" fill-opacity="0.08" stroke="{s['green']}" stroke-opacity="0.3"/>
          <text x="8" y="15">1. Add status field to data</text>
          <text x="180" y="15" text-anchor="end" fill="{s['green']}">✓</text>
        </g>
        <g transform="translate(0,26)">
          <rect width="190" height="22" rx="3" fill="{s['green']}" fill-opacity="0.08" stroke="{s['green']}" stroke-opacity="0.3"/>
          <text x="8" y="15">2. Show as plain text</text>
          <text x="180" y="15" text-anchor="end" fill="{s['green']}">✓</text>
        </g>
        <g transform="translate(0,52)">
          <rect width="190" height="22" rx="3" fill="{s['green']}" fill-opacity="0.08" stroke="{s['green']}" stroke-opacity="0.3"/>
          <text x="8" y="15">3. Make it a colored label</text>
          <text x="180" y="15" text-anchor="end" fill="{s['green']}">✓</text>
        </g>
        <g transform="translate(0,78)">
          <rect width="190" height="22" rx="3" fill="{s['green']}" fill-opacity="0.08" stroke="{s['green']}" stroke-opacity="0.3"/>
          <text x="8" y="15">4. Add filter buttons</text>
          <text x="180" y="15" text-anchor="end" fill="{s['green']}">✓</text>
        </g>
      </g>
      <text x="115" y="185" text-anchor="middle" font-size="9" fill="{s['green']}" font-weight="700">4 tiny wins</text>
    </g>
  </g>
</svg>
<figcaption>Same feature. On the left: a nightmare. On the right: normal work.</figcaption>
</figure>
"""


def feedback_loop() -> str:
    s = _S
    return f"""
<figure class="pb-figure">
<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Feedback loop: implement, test, fix, test again, validate">
{_DEFS}
  <g font-family="Inter, sans-serif" font-size="9.5" fill="{s['ink']}">
    <!-- center circle -->
    <circle cx="210" cy="110" r="46" fill="url(#gradSoft)" stroke="{s['teal']}" stroke-width="1.5"/>
    <text x="210" y="106" text-anchor="middle" font-size="10" font-weight="800" fill="{s['teal']}" letter-spacing="1">FEEDBACK</text>
    <text x="210" y="122" text-anchor="middle" font-size="10" font-weight="800" fill="{s['teal']}" letter-spacing="1">LOOP</text>

    <!-- five stations around a ring -->
    <g>
      <circle cx="210" cy="30" r="24" fill="{s['card']}" stroke="{s['teal']}"/>
      <text x="210" y="34" text-anchor="middle" font-weight="700">IMPLEMENT</text>
    </g>
    <g>
      <circle cx="360" cy="80" r="24" fill="{s['card']}" stroke="{s['teal']}"/>
      <text x="360" y="84" text-anchor="middle" font-weight="700">TEST</text>
    </g>
    <g>
      <circle cx="325" cy="180" r="24" fill="{s['card']}" stroke="{s['teal']}"/>
      <text x="325" y="184" text-anchor="middle" font-weight="700">FIX</text>
    </g>
    <g>
      <circle cx="95" cy="180" r="24" fill="{s['card']}" stroke="{s['teal']}"/>
      <text x="95" y="184" text-anchor="middle" font-weight="700">TEST AGAIN</text>
    </g>
    <g>
      <circle cx="60" cy="80" r="24" fill="{s['card']}" stroke="{s['teal']}"/>
      <text x="60" y="84" text-anchor="middle" font-weight="700">VALIDATE</text>
    </g>

    <!-- arrows -->
    <g fill="none" stroke="{s['teal']}" stroke-width="1.5" stroke-opacity="0.75">
      <path d="M234 34 A100 100 0 0 1 338 78" marker-end="url(#arr)"/>
      <path d="M354 106 A100 100 0 0 1 336 156" marker-end="url(#arr)"/>
      <path d="M301 184 L119 184" marker-end="url(#arr)"/>
      <path d="M83 158 A100 100 0 0 1 66 106" marker-end="url(#arr)"/>
      <path d="M82 78  A100 100 0 0 1 186 34" marker-end="url(#arr)"/>
    </g>
    <defs>
      <marker id="arr" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto">
        <polygon points="0,0 6,3 0,6" fill="{s['teal']}"/>
      </marker>
    </defs>
  </g>
</svg>
<figcaption>After every change: check. Then check the check. Until it really works.</figcaption>
</figure>
"""


def diff_mockup() -> str:
    s = _S
    return f"""
<figure class="pb-figure">
<svg viewBox="0 0 460 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="What a diff looks like">
{_DEFS}
  <g font-family="'JetBrains Mono', monospace" font-size="9.5">
    <!-- window chrome -->
    <rect x="10" y="10" width="440" height="200" rx="8" fill="#060C22" stroke="{s['line']}"/>
    <rect x="10" y="10" width="440" height="24" rx="8" fill="{s['card']}"/>
    <g transform="translate(20,18)">
      <circle r="4" cx="4" cy="8" fill="#F58BB6"/>
      <circle r="4" cx="18" cy="8" fill="#F5C453"/>
      <circle r="4" cx="32" cy="8" fill="#6EE7A2"/>
    </g>
    <text x="230" y="26" text-anchor="middle" fill="{s['inkMute']}" font-family="Inter" font-size="9" letter-spacing="2">applications/list.tsx</text>

    <!-- diff lines -->
    <g transform="translate(24,50)" fill="{s['ink']}">
      <text y="0" fill="{s['inkMute']}">  10  function ApplicationList() {{</text>
      <g>
        <rect x="-4" y="6" width="420" height="14" fill="#F58BB6" fill-opacity="0.14"/>
        <text y="16" fill="#F58BB6">-  11    return &lt;ul&gt;{{apps.map(...)}}&lt;/ul&gt;</text>
      </g>
      <g>
        <rect x="-4" y="22" width="420" height="14" fill="#6EE7A2" fill-opacity="0.14"/>
        <text y="32" fill="#6EE7A2">+  11    const [f, setF] = useState('all')</text>
      </g>
      <g>
        <rect x="-4" y="38" width="420" height="14" fill="#6EE7A2" fill-opacity="0.14"/>
        <text y="48" fill="#6EE7A2">+  12    const visible = apps.filter(byF(f))</text>
      </g>
      <g>
        <rect x="-4" y="54" width="420" height="14" fill="#6EE7A2" fill-opacity="0.14"/>
        <text y="64" fill="#6EE7A2">+  13    return &lt;&gt;&lt;Filter on={{f}}/&gt;&lt;List rows={{visible}}/&gt;&lt;/&gt;</text>
      </g>
      <text y="80" fill="{s['inkMute']}">  14  }}</text>
    </g>

    <!-- callouts -->
    <g font-family="Inter, sans-serif" font-size="8">
      <text x="24" y="180" fill="{s['red']}" font-weight="700">RED</text>
      <text x="52" y="180" fill="{s['inkSoft']}">= removed</text>
      <text x="140" y="180" fill="{s['green']}" font-weight="700">GREEN</text>
      <text x="178" y="180" fill="{s['inkSoft']}">= added</text>
      <text x="260" y="180" fill="{s['inkMute']}">Read each line before you approve.</text>
    </g>
  </g>
</svg>
<figcaption>A diff shows what actually changed — red went out, green came in.</figcaption>
</figure>
"""


def mistake_to_rule() -> str:
    s = _S
    return f"""
<figure class="pb-figure">
<svg viewBox="0 0 460 160" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mistake becomes rule becomes better behavior">
{_DEFS}
  <g font-family="Inter, sans-serif">
    <!-- box 1 mistake -->
    <g transform="translate(10,30)">
      <rect width="130" height="80" rx="10" fill="{s['card']}" stroke="{s['red']}" stroke-opacity="0.6"/>
      <text x="65" y="24" text-anchor="middle" font-size="10" font-weight="800" fill="{s['red']}" letter-spacing="2">MISTAKE</text>
      <foreignObject x="10" y="30" width="110" height="44">
        <div xmlns="http://www.w3.org/1999/xhtml" style="font:9px Inter; color:rgba(240,244,255,0.75); text-align:center; line-height:1.35;">Agent changed a file outside the feature.</div>
      </foreignObject>
    </g>
    <!-- arrow -->
    <path d="M140 70 L170 70" stroke="{s['teal']}" stroke-width="2"/>
    <polygon points="170,70 165,66 165,74" fill="{s['teal']}"/>
    <!-- box 2 rule -->
    <g transform="translate(170,30)">
      <rect width="130" height="80" rx="10" fill="url(#gradSoft)" stroke="{s['teal']}" stroke-width="1.5"/>
      <text x="65" y="24" text-anchor="middle" font-size="10" font-weight="800" fill="{s['teal']}" letter-spacing="2">NEW RULE</text>
      <foreignObject x="8" y="30" width="114" height="44">
        <div xmlns="http://www.w3.org/1999/xhtml" style="font:8.5px Inter; color:{s['ink']}; text-align:center; line-height:1.3;">"Don't touch files outside the feature. Ask if unsure."</div>
      </foreignObject>
    </g>
    <!-- arrow -->
    <path d="M300 70 L330 70" stroke="{s['green']}" stroke-width="2"/>
    <polygon points="330,70 325,66 325,74" fill="{s['green']}"/>
    <!-- box 3 better -->
    <g transform="translate(330,30)">
      <rect width="120" height="80" rx="10" fill="{s['card']}" stroke="{s['green']}" stroke-width="1.5"/>
      <text x="60" y="24" text-anchor="middle" font-size="10" font-weight="800" fill="{s['green']}" letter-spacing="2">NEXT TIME</text>
      <foreignObject x="6" y="30" width="108" height="44">
        <div xmlns="http://www.w3.org/1999/xhtml" style="font:9px Inter; color:{s['ink']}; text-align:center; line-height:1.35;">Agent stays in scope. Mistake never returns.</div>
      </foreignObject>
    </g>

    <text x="230" y="146" text-anchor="middle" font-size="9" fill="{s['inkMute']}" font-family="Inter" letter-spacing="1">Write it once. Every future session gets it for free.</text>
  </g>
</svg>
<figcaption>Every surprise is free training data — if you write the rule down.</figcaption>
</figure>
"""


def walkthrough_timeline() -> str:
    s = _S
    steps = [
        ("Define",      "Write objective + scope + done."),
        ("Context",     "Point to project memory."),
        ("Investigate", "Ask agent to summarize first."),
        ("Boundaries",  "Say what NOT to touch."),
        ("Execute",     "Step 1, then step 2."),
        ("Verify",      "Click. Test. Try edge case."),
        ("Review",      "Read the diff line by line."),
        ("Learn",       "Add one new rule."),
    ]
    boxes = ""
    for i, (name, desc) in enumerate(steps):
        x = 15 + i * 55
        boxes += f"""
    <g transform="translate({x},50)">
      <circle cx="20" cy="20" r="16" fill="{s['card']}" stroke="{s['teal']}" stroke-width="1.5"/>
      <text x="20" y="24" text-anchor="middle" font-size="10" font-weight="800" fill="{s['teal']}">{i+1}</text>
      <text x="20" y="55" text-anchor="middle" font-size="8.5" font-weight="700" fill="{s['ink']}" font-family="Inter">{name}</text>
      <foreignObject x="-8" y="60" width="56" height="40">
        <div xmlns="http://www.w3.org/1999/xhtml" style="font:7.5px Inter; color:rgba(240,244,255,0.65); text-align:center; line-height:1.3;">{desc}</div>
      </foreignObject>
    </g>
"""
        if i < len(steps) - 1:
            boxes += f'\n    <line x1="{x+36}" y1="70" x2="{x+55+4}" y2="70" stroke="{s["teal"]}" stroke-width="1.5" stroke-dasharray="3 2" opacity="0.6"/>\n'
    return f"""
<figure class="pb-figure">
<svg viewBox="0 0 470 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="One task, eight stops">
{_DEFS}
  <text x="15" y="30" font-family="Inter" font-size="10" fill="{s['inkMute']}" letter-spacing="3">ONE FEATURE · EIGHT STOPS</text>
  {boxes}
</svg>
<figcaption>Each stage is small. Together they turn a wish into a shipped feature.</figcaption>
</figure>
"""


def task_template_visual() -> str:
    s = _S
    fields = [
        ("Task",             "One-line name."),
        ("Goal",             "The outcome — why it matters."),
        ("Context",          "Which folders / files."),
        ("Inspect first",    "Ask the agent to look before it leaps."),
        ("Scope",            "What may change."),
        ("Boundaries",       "What must NOT change."),
        ("Success criteria", "Checkable list of what 'done' looks like."),
        ("Validation",       "How you'll prove it works."),
        ("Review",           "What you'll read in the diff."),
    ]
    rows = ""
    for i, (label, hint) in enumerate(fields):
        y = 40 + i * 30
        rows += f"""
    <g transform="translate(20,{y})">
      <rect width="420" height="24" rx="4" fill="{s['card']}" stroke="{s['line']}"/>
      <rect width="6" height="24" rx="0" fill="url(#grad)"/>
      <text x="16" y="16" font-size="9" font-weight="800" fill="{s['teal']}" letter-spacing="1">{label.upper()}</text>
      <text x="130" y="16" font-size="9" fill="{s['inkSoft']}" font-style="italic">{hint}</text>
    </g>
"""
    return f"""
<figure class="pb-figure pb-figure--full">
<svg viewBox="0 0 460 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Task template as a form">
{_DEFS}
  <g font-family="Inter, sans-serif">
    <text x="20" y="24" font-size="12" font-weight="800" fill="{s['ink']}">AI Coding Task · fill in the blanks</text>
    {rows}
  </g>
</svg>
<figcaption>Print it. Fill it. Do it before every task, until you don't need the form.</figcaption>
</figure>
"""


def why_ai_breaks() -> str:
    s = _S
    return f"""
<figure class="pb-figure">
<svg viewBox="0 0 460 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A vague prompt vs a working project">
{_DEFS}
  <g font-family="Inter, sans-serif">
    <!-- prompt -->
    <g transform="translate(20,30)">
      <rect width="150" height="60" rx="8" fill="{s['card']}" stroke="{s['line']}"/>
      <text x="12" y="22" font-size="9" fill="{s['inkMute']}" letter-spacing="2">YOU TYPE</text>
      <text x="12" y="42" font-size="10" fill="{s['ink']}">"Add rejected status"</text>
    </g>
    <!-- arrow -->
    <path d="M175 60 L215 60" stroke="{s['teal']}" stroke-width="2"/>
    <polygon points="215,60 210,56 210,64" fill="{s['teal']}"/>
    <!-- ai -->
    <g transform="translate(215,20)">
      <rect width="80" height="80" rx="10" fill="url(#gradSoft)" stroke="{s['teal']}" stroke-width="1.5"/>
      <text x="40" y="30" text-anchor="middle" font-size="9" font-weight="800" fill="{s['teal']}" letter-spacing="2">AGENT</text>
      <text x="40" y="52" text-anchor="middle" font-size="18">⚙</text>
      <text x="40" y="70" text-anchor="middle" font-size="8" fill="{s['inkSoft']}">400 lines</text>
    </g>
    <!-- arrow -->
    <path d="M300 60 L340 60" stroke="{s['red']}" stroke-width="2"/>
    <polygon points="340,60 335,56 335,64" fill="{s['red']}"/>
    <!-- broken -->
    <g transform="translate(340,20)">
      <rect width="110" height="80" rx="10" fill="{s['card']}" stroke="{s['red']}"/>
      <text x="55" y="28" text-anchor="middle" font-size="9" fill="{s['red']}" font-weight="800" letter-spacing="2">BROKEN</text>
      <text x="15" y="46" font-size="8.5" fill="{s['inkSoft']}">✗ New page blank</text>
      <text x="15" y="60" font-size="8.5" fill="{s['inkSoft']}">✗ List broke</text>
      <text x="15" y="74" font-size="8.5" fill="{s['inkSoft']}">✗ Can't undo</text>
    </g>

    <!-- the missing layer -->
    <g transform="translate(20,130)">
      <rect width="430" height="52" rx="8" fill="url(#gradSoft)" stroke="{s['teal']}" stroke-width="1.5" stroke-dasharray="4 3"/>
      <text x="215" y="22" text-anchor="middle" font-size="10" font-weight="800" fill="{s['teal']}" letter-spacing="3">WHAT WAS MISSING</text>
      <text x="215" y="40" text-anchor="middle" font-size="9.5" fill="{s['ink']}">Task · Scope · Boundaries · Definition of done · Verification · Review</text>
    </g>
  </g>
</svg>
<figcaption>The prompt wasn't wrong. Everything around the prompt was missing.</figcaption>
</figure>
"""


def prompt_vs_workflow() -> str:
    s = _S
    return f"""
<figure class="pb-figure">
<svg viewBox="0 0 460 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A prompt is one instruction; a workflow is a system">
{_DEFS}
  <g font-family="Inter, sans-serif">
    <!-- left: prompt -->
    <g transform="translate(20,20)">
      <rect width="180" height="170" rx="10" fill="{s['card']}" stroke="{s['line']}"/>
      <text x="90" y="26" text-anchor="middle" font-size="10" font-weight="800" fill="{s['inkMute']}" letter-spacing="3">A PROMPT</text>
      <text x="90" y="42" text-anchor="middle" font-size="8" fill="{s['inkMute']}">one instruction</text>
      <g transform="translate(50,66)">
        <rect width="80" height="26" rx="4" fill="{s['blue']}" fill-opacity="0.16" stroke="{s['blue']}" stroke-opacity="0.4"/>
        <text x="40" y="17" text-anchor="middle" font-size="9" fill="{s['ink']}">"Fix the bug"</text>
      </g>
      <g transform="translate(20,110)" fill="{s['inkSoft']}" font-size="8.5">
        <text x="0" y="0">Life-span: minutes</text>
        <text x="0" y="14">Blast radius: one reply</text>
        <text x="0" y="28">Repeatable: no</text>
        <text x="0" y="42">Compounds: no</text>
      </g>
    </g>
    <!-- right: workflow -->
    <g transform="translate(230,20)">
      <rect width="210" height="170" rx="10" fill="url(#gradSoft)" stroke="{s['teal']}" stroke-width="1.5"/>
      <text x="105" y="26" text-anchor="middle" font-size="10" font-weight="800" fill="{s['teal']}" letter-spacing="3">A WORKFLOW</text>
      <text x="105" y="42" text-anchor="middle" font-size="8" fill="{s['inkMute']}">a system around the instruction</text>
      <g transform="translate(16,60)" font-size="8" fill="{s['ink']}">
        <text x="0" y="0">Define · Context · Investigate</text>
        <text x="0" y="12">Boundaries · Execute · Verify</text>
        <text x="0" y="24">Review · Learn</text>
      </g>
      <g transform="translate(16,110)" fill="{s['inkSoft']}" font-size="8.5">
        <text x="0" y="0">Life-span: the whole project</text>
        <text x="0" y="14">Blast radius: every change (in a good way)</text>
        <text x="0" y="28">Repeatable: yes</text>
        <text x="0" y="42">Compounds: yes</text>
      </g>
    </g>
  </g>
</svg>
<figcaption>Prompt is a sentence. Workflow is the working environment around that sentence.</figcaption>
</figure>
"""


DIAGRAMS_BY_CHAPTER = {
    "03": why_ai_breaks,
    "04": chatbot_vs_agent,
    "05": chatbot_vs_agent,
    "06": prompt_vs_workflow,
    "07": framework_flow,
    "10": blast_radius,
    "14": investigate_pipeline,
    "16": small_vs_big,
    "18": blast_radius,
    "21": feedback_loop,
    "24": diff_mockup,
    "26": mistake_to_rule,
    "28": framework_flow,
    "29": walkthrough_timeline,
    "30": task_template_visual,
}
