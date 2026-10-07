"""Rebuild the profile dashboard SVGs. Standard-library Python only."""
from pathlib import Path
from html import escape
import textwrap

ROOT = Path(__file__).parent / 'assets'
ROOT.mkdir(exist_ok=True)
BG, CARD, BORDER, WHITE, MUTED, BLUE, GREEN = '#0d1117', '#131b23', '#27323d', '#eef3f8', '#b9c3ce', '#79b8ff', '#80d58a'

def start(w,h,title):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><rect width="{w}" height="{h}" rx="16" fill="{BG}"/><g font-family="DejaVu Sans,Arial,sans-serif">']
def txt(a,x,y,s,size=20,color=MUTED,weight=400):
    a.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(s)}</text>')
def rule(a,x,y,w):
    a.append(f'<path d="M{x} {y}h{w}" stroke="{BORDER}"/>')
def icon(a,x,y,kind,color=BLUE,s=30):
    shapes={
        'shield':'<path d="M16 3l11 4v9c0 7-5 12-11 15C10 28 5 23 5 16V7z"/>',
        'brain':'<path d="M15 7c-7-7-14 2-9 7-7 4-4 13 2 13 0 7 9 7 9 0V6m3 1c7-7 14 2 9 7 7 4 4 13-2 13 0 7-9 7-9 0V6M8 16l5 3m11-3-5 3M9 26l5-3m9 3-4-3"/>',
        'gear':'<path d="M13 3h6l1 5 4 2 5-1 3 5-4 4v4l3 4-3 5-5-2-4 2-1 5h-6l-1-5-4-2-5 2-3-5 3-4v-4l-4-4 3-5 5 1 4-2z"/><circle cx="16" cy="19" r="5"/>',
        'book':'<path d="M16 7C10 3 5 3 1 5v24c5-2 10-2 15 2 5-4 10-4 15-2V5c-4-2-9-2-15 2zM16 7v24"/>',
        'search':'<circle cx="13" cy="13" r="10"/><path d="M21 21l10 10"/>',
        'target':'<circle cx="16" cy="16" r="13"/><circle cx="16" cy="16" r="7"/><path d="M16 16L30 2m-1 0v7h-7"/>',
        'database':'<ellipse cx="16" cy="6" rx="12" ry="4"/><path d="M4 6v21c0 6 24 6 24 0V6M4 16c0 6 24 6 24 0"/>',
        'leaf':'<path d="M29 3C5 3 0 15 7 24s25 4 22-21zM3 32L23 10"/>',
        'file':'<path d="M6 2h14l8 8v22H6zM20 2v9h8M11 17h12m-12 6h12"/>'}
    a.append(f'<g transform="translate({x} {y}) scale({s/36})" fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">{shapes[kind]}</g>')
def lines(a,x,y,text,width,size=20,leading=30,color=MUTED):
    for i,line in enumerate(textwrap.wrap(text,width)):
        txt(a,x,y+i*leading,line,size,color)
    return y+len(textwrap.wrap(text,width))*leading
def heading(a,x,y,text,kind,w):
    icon(a,x,y-28,kind,s=30);txt(a,x+44,y,text,26,WHITE,600);rule(a,x,y+15,w)
def rect(a,x,y,w,h):
    a.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{CARD}" stroke="{BORDER}"/>')

projects=[('JoeyOS','brain',BLUE,'Personal AI / Knowledge OS','An AI-native personal knowledge operating system designed to become a persistent context and intelligence layer across tools, models, and time.',['PKM','AI Agents','Systems']),('Safety Intelligence','shield',GREEN,'AI × Risk × Real-world Impact','Exploring how AI can strengthen safety and operational risk management through data, systems and better decision support.',['Safety','Risk','Analytics']),('AI Workflows','gear',BLUE,'Tools / Agents / Automation','Building small, purpose-built tools, agents and workflows that improve professional judgment and support recurring work.',['Agents','Automation','Tools'])]
questions=['Can AI identify weak signals before they become incidents?','How can organizational experience become reusable intelligence?','How should humans and AI work together when judgment matters?','What does a knowledge system look like with AI as a permanent collaborator?']
approach=['Observe the signal','Preserve the context','Improve the decision','Capture the learning']
current=[('JoeyOS','book',BLUE,'Personal knowledge infrastructure for the AI era.'),('Safety Intelligence Lab','shield',GREEN,'AI × safety × risk experiments and frameworks.'),('AI Workflows','gear',BLUE,'Agents, skills and repeatable automation tools.'),('Field Notes','file',BLUE,'Research, frameworks, lessons and ideas.')]

def dashboard(mobile=False):
    w,h=(640,2590) if mobile else (1200,1170)
    a=start(w,h,"Joey Yang Lab dashboard: safety systems, AI and knowledge infrastructure")
    x=28
    txt(a,x,65,"Hey, I’m Joey",42,WHITE,700)
    txt(a,x,105,'Safety Systems × AI × Knowledge Infrastructure',21,WHITE,600)
    if mobile:
        y=lines(a,x,153,'I work at the intersection of safety, operational risk, AI, and knowledge systems. My main interest is simple:',45,21,32)
        y=lines(a,x+18,y+25,'How can better systems help us recognize risk earlier, make better decisions, and turn experience into reusable intelligence?',42,21,32,BLUE)
        y=lines(a,x,y+28,'GitHub is my public lab for exploring that question.',45,21,32)
        domains_y=y+25
        for i,(name,sub,k,c) in enumerate([('SAFETY','People · Assets · Operations','shield',BLUE),('AI & AGENTS','Tools · Workflows · Intelligence','gear',BLUE),('KNOWLEDGE SYSTEMS','Capture · Distill · Connect · Evolve','database',BLUE),('SUSTAINABILITY','Safer · Smarter · More Resilient','leaf',GREEN)]):
            dy=domains_y+i*64;icon(a,x,dy,k,c,32);txt(a,x+48,dy+18,name,19,WHITE,600);txt(a,x+48,dy+43,sub,18)
        build_y=domains_y+300
    else:
        lines(a,x,160,'I work at the intersection of safety, operational risk, AI, and knowledge systems. My main interest is simple:',76,19,29)
        lines(a,x+24,240,'How can better systems help us recognize risk earlier, make better decisions, and turn experience into reusable intelligence?',71,20,31,BLUE)
        a.append(f'<path d="M{ x+4 } 215v90" stroke="{BLUE}" stroke-width="2"/>')
        txt(a,x,344,'GitHub is my public lab for exploring that question.',20)
        a.append(f'<path d="M872 42v310" stroke="{BORDER}"/>')
        for i,(name,sub,k,c) in enumerate([('SAFETY','People · Assets · Operations','shield',BLUE),('AI & AGENTS','Tools · Workflows · Intelligence','gear',BLUE),('KNOWLEDGE SYSTEMS','Capture · Distill · Connect · Evolve','database',BLUE),('SUSTAINABILITY','Safer · Smarter · More Resilient','leaf',GREEN)]):
            dy=52+i*74;icon(a,895,dy,k,c,32);txt(a,942,dy+18,name,17,WHITE,600);txt(a,942,dy+44,sub,13)
        build_y=405
    heading(a,x,build_y,'What I’m Building','gear',w-56)
    card_y=build_y+38
    for i,(name,k,c,sub,desc,tags) in enumerate(projects):
        cx=x if mobile else x+i*386;cy=card_y+i*352 if mobile else card_y;cw=584 if mobile else 372;ch=326 if mobile else 362
        rect(a,cx,cy,cw,ch);icon(a,cx+22,cy+24,k,c,42)
        txt(a,cx+82,cy+44,name,24 if mobile else 21,BLUE,600)
        txt(a,cx+82,cy+74,sub,19 if mobile else 16,BLUE)
        lines(a,cx+24,cy+120,desc,45 if mobile else 28,21 if mobile else 19,31)
        px=cx+24
        for tag in tags:
            tw=len(tag)*9+30;a.append(f'<rect x="{px}" y="{cy+ch-48}" width="{tw}" height="30" rx="15" fill="#1c2631" stroke="{BORDER}"/>');txt(a,px+15,cy+ch-27,tag,15,WHITE);px+=tw+12
    q_y=card_y+1094 if mobile else card_y+412
    heading(a,x,q_y,'Key Questions I’m Exploring','search',w-56 if mobile else 820)
    yy=q_y+48
    for q in questions:
        txt(a,x+3,yy,'•',22,BLUE); yy=lines(a,x+28,yy,q,43 if mobile else 75,21 if mobile else 18,31)+12
    ax,ay=(x,yy+36) if mobile else (900,q_y)
    heading(a,ax,ay,'My Approach','target',w-56 if mobile else 272)
    for i,s in enumerate(approach):
        txt(a,ax+8,ay+48+i*33,'•',22,BLUE);txt(a,ax+34,ay+48+i*33,s,21 if mobile else 18)
    cur_y=ay+215 if mobile else q_y+242
    heading(a,x,cur_y,'Current Projects','book',w-56)
    for i,(name,k,c,desc) in enumerate(current):
        cx=x+(i%2)*300 if mobile else x+i*289;cy=cur_y+36+(i//2)*151 if mobile else cur_y+36;cw=284 if mobile else 276
        rect(a,cx,cy,cw,135);icon(a,cx+16,cy+18,k,c,30)
        txt(a,cx+55,cy+38,name,17 if mobile else 16,WHITE,600)
        lines(a,cx+18,cy+74,desc,23,16,23)
    footer_y=cur_y+366 if mobile else cur_y+209
    rule(a,x,footer_y,w-56)
    txt(a,x,footer_y+44,'Joey Yang Lab',25,WHITE,600)
    if mobile:
        lines(a,x,footer_y+81,'Building safer systems. Thinking across disciplines. Turning experience into intelligence.',46,18,29,BLUE)
    else:
        txt(a,265,footer_y+43,'Building safer systems. Thinking across disciplines. Turning experience into intelligence.',16,BLUE)
    a.append('</g></svg>')
    # Fit the canvas tightly around the completed layout.
    result=''.join(a); actual=footer_y+(165 if mobile else 80)
    result=result.replace(f'height="{h}"',f'height="{actual}"').replace(f'0 0 {w} {h}',f'0 0 {w} {actual}')
    return result

def banner(mobile=False):
    w,h=(640,360) if mobile else (1440,280);a=start(w,h,'Joey Yang Lab — From risk signals to better decisions. From experience to intelligence.')
    a.insert(1,'<defs><linearGradient id="sky" x2="0" y2="1"><stop stop-color="#17334e"/><stop offset="1" stop-color="#c18b59"/></linearGradient><linearGradient id="fade"><stop stop-color="#0d1117" stop-opacity="0"/><stop offset="1" stop-color="#0d1117"/></linearGradient></defs>')
    if not mobile:
        a.append('<rect width="460" height="280" fill="url(#sky)"/><circle cx="217" cy="99" r="23" fill="#f8d7a1"/><path d="M0 165L129 105 369 143 449 178 219 139 0 190" fill="#81929f"/><path d="M0 190l219-51v124L0 280z" fill="#435563"/><path d="M219 139l230 39v88l-230-3z" fill="#293845"/>')
        for i in range(10): a.append(f'<path d="M{10+i*20} 185v80" stroke="#82909b" opacity=".4"/>')
        a.append('<rect width="510" height="280" fill="url(#fade)"/>')
        for i in range(6):
            a.append(f'<ellipse cx="1230" cy="115" rx="{32+i*15}" ry="86" fill="none" stroke="#245589" opacity=".45"/><ellipse cx="1230" cy="115" rx="106" ry="{16+i*14}" fill="none" stroke="#245589" opacity=".45"/>')
        tx=405;txt(a,tx,83,'JOEY YANG',43,WHITE,700);txt(a,tx+274,83,'LAB',43,BLUE,700)
        txt(a,tx,120,'SAFETY SYSTEMS × AI × KNOWLEDGE INFRASTRUCTURE',17,WHITE,600)
        txt(a,tx,174,'From risk signals to better decisions.',21,WHITE)
        txt(a,tx,204,'From experience to intelligence.',21,BLUE)
        pts=[(861,242),(980,206),(1100,238),(1230,254),(1368,224)]
        a.append('<path d="M820 250C900 275 920 169 1030 213S1160 284 1230 254 1340 193 1440 239" fill="none" stroke="#3684c9" stroke-width="2"/>')
        for (px,py),label in zip(pts,['SIGNALS','CONTEXT','JUDGMENT','DECISION','LEARNING']):
            a.append(f'<circle cx="{px}" cy="{py}" r="5" fill="#a9dcff"/>');txt(a,px-28,py-19,label,11,WHITE)
    else:
        txt(a,28,67,'JOEY YANG LAB',39,WHITE,700)
        txt(a,28,111,'Safety Systems × AI',23,BLUE,600)
        txt(a,28,147,'× Knowledge Infrastructure',23,BLUE,600)
        txt(a,28,210,'From risk signals to better decisions.',24,WHITE)
        txt(a,28,248,'From experience to intelligence.',24,BLUE)
        txt(a,28,317,'Signals → Context → Judgment → Decision → Learning',17,MUTED)
    a.append('</g></svg>');return ''.join(a)

for name,svg in [('lab-dashboard.svg',dashboard()),('lab-dashboard-mobile.svg',dashboard(True)),('lab-banner.svg',banner()),('lab-banner-mobile.svg',banner(True))]:
    (ROOT/name).write_text(svg)
