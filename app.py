import streamlit as st
import folium
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
        # Insert data using the following template
                #{
                    # name
                    # lat
                    # lng
                    # color
                    # tag
                    # summary
                    # bullets: []
                #}
    {

        "name": "Wayne County, MI",
        "lat": 42.35,
        "lng": -83.15,
        "color": "darkblue",
        "tag": "Formal MPZ Coalition",
        "summary": "Southeast Michigan is one of the nation's most promising MPZ candidates.",
        "bullets": [
            "Detroit/Wayne County Port Authority leading formal MPZ bid",
            "University of Michigan — naval architecture + marine engineering",
            "Macomb Community College — $15.4M Navy maritime welding investment",
            "30+ org coalition across 4 counties",
            "Part of $50M Michigan Maritime Manufacturing Initiative"
        ]
    },
]

locations_json = json.dumps(locations)

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

const colorMap = {{
    'darkblue': '#1a3d6b',
    'blue': '#2196F3',
    'green': '#4CAF50',
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

function showPanel(index) {{
    const loc = locations[index];
    if (!loc) return;

    document.getElementById('default-msg').style.display = 'none';
    const content = document.getElementById('panel-content');
    content.style.display = 'block';

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
}}

locations.forEach(function(loc, i) {{
    const marker = L.marker([loc.lat, loc.lng], {{
        icon: L.divIcon({{
            className: '',
            html: `<div style="
                background: ${{colorMap[loc.color] || '#2196F3'}};
                width: 32px; height: 32px;
                border-radius: 50% 50% 50% 0;
                transform: rotate(-45deg);
                border: 3px solid white;
                display: flex; align-items: center; justify-content: center;
            "><i class="fa fa-ship" style="transform: rotate(45deg); color: white; font-size: 12px;"></i></div>`,
            iconSize: [32, 32],
            iconAnchor: [16, 32],
        }})
    }}).addTo(map);

    marker.on('click', function() {{
        showPanel(i);
    }});
}});
</script>

</body>
</html>
""", height=1200, scrolling=False)