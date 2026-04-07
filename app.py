import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(layout="wide", page_title="Maritime Prosperity Zones 2026")

st.markdown("""
<style>
    .main > div { padding: 0 !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header { visibility: hidden; }
    .stApp { overflow: hidden; }
</style>
""", unsafe_allow_html=True)

locations = [
    {
        "name": "Wayne County, MI",
        "lat": 42.35,
        "lng": -83.15,
        "color": "#1a3d6b",
        "tag": "Formal MPZ Coalition",
        "summary": "Opportunity Score: High \n MPZ Status: Strong Candidate",
        "bullets": [
            "Supporting County: Wayne County, MI",
            "Port Detroit generates 6,000 jobs and $36B in economic activity",
            "713,900 total jobs in Wayne County which is the highest in Michigan",
            "Average weekly wage of $1,597 ",
            "94 designated OZs, the most of any county in Michigan",
            "OZ median household income ranges from $9,000 to $82,000",
            "Detroit Port Authority received $25.1M EPA Clean Ports grant",
            "Port of Detroit is Michigan's largest inland port with 29 terminals",
            "Part of $50M Michigan Maritime Manufacturing Initiative with U.S. Navy",
            "Michigan launched first-ever 10-year Maritime Strategy Jan 2026",
            "Formal MPZ coalition submitted with 30+ organizations"
        ]
    },
    {
        "name": "Macomb County, MI",
        "lat": 42.67,
        "lng": -82.91,
        "color": "#1a3d6b",
        "tag": "Formal MPZ Coalition",
        "summary": "Opportunity Score: High \n MPZ Status: Strong Candidate",
        "bullets": [
            "Supporting County: Macomb County, MI",
            "Macomb Community College which can be set up as the workforce anchor of SE Michigan MPZ coalition",
            "$15.4M Navy investment to fast-track maritime welding and machining program",
            "Up to 200 students graduating per year from maritime skilled trades program",
            "M3 Initiative launched at Macomb Community College by Secretary of the Navy",
            "Accu-Tech Manufacturing and NTL Industries are key Macomb County industrial partners",
            "Arsenal Alliance - regional Sterling Heights/Warren defense industry initiative",
            "Part of the 30+ org formal MPZ coalition across 4 counties"
        ]
    },
    {
        "name": "Mobile, AL",
        "lat": 30.69,
        "lng": -88.04,
        "color": "#1a5c2a",
        "tag": "Proof of Concept",
        "summary": "Opportunity Score: High \n MPZ Status: Proof of Concept",
        "bullets": [
            "Supporting County: Mobile County, AL",
            "Pinto Island is a 355 acre shipyard acquired inside an Opportunity Zone",
            "U.S. Navy partnership with OZ fund in 2024",
            "Building Columbia and Virginia class nuclear submarines",
            "Up to 3,000 jobs created",
            "Cited by White House as model for Maritime Prosperity Zones"
        ]
    },

    {
        "name": "Washtenaw County, MI",
        "lat": 42.2519,
        "lng": -83.7654,
        "color": "#1a3d6b",
        "tag": "Formal MPZ Coalition",
        "summary": "Opportunity Score: High \n MPZ Status: Strong Candidate",
        "bullets": [
            "Home to University of Michigan, #1 ranked Naval Architecture and Marine Engineering program in the U.S.",
            "UM established BRIDGE fellowship with $5.3M Navy Maritime Industrial Base Program contract",
            "1,800+ NA&ME graduates over 30 years including 800+ doctoral students",
            "Prof. Thomas McKenney co-led SE Michigan MPZ coalition and Michigan's 10-year Maritime Strategy",
            "Region provides access to iron mines, limestone quarries, St. Lawrence Seaway, and two major ports",
            "Port of Detroit collaborating with UM on nuclear, biofuel, and hydrogen powered barge technologies",
            "Only NA&ME program in the U.S. spanning undergraduate through PhD"
        ]
    },

]

institutions = [
    {
        "name": "University of Michigan",
        "lat": 42.2780,
        "lng": -83.7382,
        "type": "academic",
        "role": "Naval architecture + marine engineering"
    },
    {
        "name": "Macomb Community College",
        "lat": 42.5784,
        "lng": -82.9238,
        "type": "academic",
        "role": "$15.4M Navy investment + maritime welding and machining program"
    },
    {
        "name": "Oakland Community College",
        "lat": 42.5412,
        "lng": -83.2913,
        "type": "academic",
        "role": "M3 Initiative academic partner + accelerated "
    },
    {
        "name": "Detroit/Wayne County Port Authority",
        "lat": 42.3314,
        "lng": -83.0457,
        "type": "government",
        "role": "Leading formal MPZ coalition bid + Michigan's largest inland port"
    },
    {
        "name": "Newlab Detroit",
        "lat": 42.3314,
        "lng": -83.0580,
        "type": "industry",
        "role": "Maritime startup hub, converting early momentum into commercial activity"
    },
    {
        "name": "LIFT Detroit",
        "lat": 42.3370,
        "lng": -83.0480,
        "type": "industry",
        "role": "Lightweight Innovations for Tomorrow, advanced manufacturing partner"
    },
    {
        "name": "Arsenal Alliance",
        "lat": 42.5803,
        "lng": -83.0302,
        "type": "industry",
        "role": "Sterling Heights/Warren regional defense industry initiative"
    },
    {
        "name": "Ann Arbor SPARK",
        "lat": 42.2808,
        "lng": -83.7430,
        "type": "industry",
        "role": "Maritime innovation ecosystem partner in SE Michigan MPZ coalition"
    },
    {
        "name": "Fincantieri Marinette Marine",
        "lat": 45.0980,
        "lng": -87.6290,
        "type": "industry",
        "role": "World-class Navy shipbuilder, the anchor of Great Lakes Shipyard Alliance"
    },
]

locations_json = json.dumps(locations)
institutions_json = json.dumps(institutions)

components.html(f"""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: Arial, sans-serif; overflow: hidden; background: #000; }}

    .banner {{
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 9999;
        background: black;
        color: white;
        padding: 20px 24px;
        font-size: 28px;
        font-weight: 600;
        letter-spacing: 0.5px;
        height: 70px;
        display: flex;
        align-items: center;
    }}

    #map {{
        position: fixed;
        top: 70px;
        left: 0; right: 0; bottom: 0;
        z-index: 1;
    }}

    .info-panel {{
        position: fixed;
        top: 95px;
        right: 20px;
        width: 300px;
        max-height: calc(100vh - 115px);
        background: rgba(10, 10, 10, 0.88);
        backdrop-filter: blur(6px);
        color: white;
        border-radius: 16px;
        padding: 20px;
        z-index: 9999;
        font-size: 14px;
        line-height: 1.7;
        overflow-y: auto;
        border: 1px solid rgba(255,255,255,0.08);
    }}

    .default-msg h4 {{
        font-size: 15px;
        font-weight: 600;
        color: white;
        margin-bottom: 8px;
    }}

    .default-msg p {{
        color: #aaa;
        font-size: 13px;
        line-height: 1.6;
    }}

    .panel-content {{ display: none; }}

    .tag {{
        display: inline-block;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        margin-bottom: 12px;
        letter-spacing: 0.3px;
    }}

    .tag-formal {{ background: #0C447C; color: #B5D4F4; }}
    .tag-active {{ background: #1a4a1a; color: #90d490; }}
    .tag-proof  {{ background: #4a3a00; color: #f0c040; }}
    .tag-institution {{ background: #2a2a2a; color: #aaa; }}

    .panel-content h2 {{
        font-size: 17px;
        font-weight: 600;
        color: white;
        margin-bottom: 8px;
        line-height: 1.3;
    }}

    .summary {{
        font-size: 13px;
        color: #aaa;
        line-height: 1.6;
        margin-bottom: 14px;
        padding-bottom: 14px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }}

    .bullets-title {{
        font-size: 11px;
        font-weight: 600;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 10px;
    }}

    .bullet-item {{
        display: flex;
        align-items: flex-start;
        gap: 10px;
        margin-bottom: 10px;
        font-size: 13px;
        color: #ccc;
        line-height: 1.5;
    }}

    .bullet-dot {{
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #378ADD;
        margin-top: 6px;
        flex-shrink: 0;
    }}
</style>
</head>
<body>

<div class="banner">Maritime Prosperity Zones 2026</div>
<div id="map"></div>

<div class="info-panel" id="info-panel">
    <div class="default-msg" id="default-msg">
        <h4>Click a pin</h4>
        <p>Select a location on the map to see MPZ activity details.</p>
    </div>
    <div class="panel-content" id="panel-content">
        <div id="panel-tag" class="tag"></div>
        <h2 id="panel-title"></h2>
        <p class="summary" id="panel-summary"></p>
        <div class="bullets-title">Key activity</div>
        <div id="panel-bullets"></div>
    </div>
</div>

<script>
const locations = {locations_json};
const institutions = {institutions_json};

const iconMap = {{
    'academic':   'fa-graduation-cap',
    'government': 'fa-university',
    'industry':   'fa-industry',
}};

const map = L.map('map').setView([39, -96], 4);

L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
    attribution: '© OpenStreetMap contributors'
}}).addTo(map);

function getTagClass(tag) {{
    if (tag.includes('Formal')) return 'tag-formal';
    if (tag.includes('Active')) return 'tag-active';
    if (tag.includes('Proof'))  return 'tag-proof';
    return 'tag-formal';
}}

function showPanel(index, type) {{
    document.getElementById('default-msg').style.display = 'none';
    const content = document.getElementById('panel-content');
    content.style.display = 'block';

    if (type === 'location') {{
        const loc = locations[index];
        const tag = document.getElementById('panel-tag');
        tag.textContent = loc.tag;
        tag.className = 'tag ' + getTagClass(loc.tag);
        document.getElementById('panel-title').textContent = loc.name;
        document.getElementById('panel-summary').textContent = loc.summary;
        const bulletsDiv = document.getElementById('panel-bullets');
        bulletsDiv.innerHTML = loc.bullets.map(b => `
            <div class="bullet-item">
                <div class="bullet-dot"></div>
                <span>${{b}}</span>
            </div>
        `).join('');
    }} else {{
        const inst = institutions[index];
        const tag = document.getElementById('panel-tag');
        tag.textContent = inst.type.charAt(0).toUpperCase() + inst.type.slice(1);
        tag.className = 'tag tag-institution';
        document.getElementById('panel-title').textContent = inst.name;
        document.getElementById('panel-summary').textContent = inst.role;
        document.getElementById('panel-bullets').innerHTML = '';
    }}
}}

locations.forEach(function(loc, i) {{
    const marker = L.marker([loc.lat, loc.lng], {{
        icon: L.divIcon({{
            className: '',
            html: `<div style="
            background: ${{loc.color}};
            width: 42px; height: 42px;
            border-radius: 50% 50% 50% 0;
            transform: rotate(-45deg);
            border: 2px solid rgba(255,255,255,0.6);
            display: flex; align-items: center; justify-content: center;
            "><i class="fa fa-ship" style="transform: rotate(45deg); color: white; font-size: 16px;"></i></div>`,
            iconSize: [42, 42],
            iconAnchor: [21, 42],   
                }})
    }}).addTo(map);
    marker.on('click', function() {{ showPanel(i, 'location'); }});
}});

institutions.forEach(function(inst, i) {{
    const marker = L.marker([inst.lat, inst.lng], {{
        icon: L.divIcon({{
            className: '',
            html: `<div style="
                background: #111;
                width: 28px; height: 28px;
                border-radius: 50%;
                border: 2px solid rgba(255,255,255,0.4);
                display: flex; align-items: center; justify-content: center;
            "><i class="fa ${{iconMap[inst.type]}}" style="color: white; font-size: 11px;"></i></div>`,
            iconSize: [28, 28],
            iconAnchor: [14, 14],
        }})
    }}).addTo(map);
    marker.on('click', function() {{ showPanel(i, 'institution'); }});
}});
</script>

</body>
</html>
""", height=1200, scrolling=False)