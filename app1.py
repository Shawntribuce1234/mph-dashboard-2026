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
    {
        "name": "Marinette County, WI",
        "lat": 45.10,
        "lng": -87.63,
        "color": "#1a3d6b",
        "tag": "Formal MPZ Coalition",
        "summary": "Opportunity Score: High \n MPZ Status: Strong Candidate",
        "bullets": [
            "3,000 employees across 3 Wisconsin shipyards, ~1,000 in Marinette County alone",
            "Manufacturing accounts for 29% of all jobs in Marinette County",
            "$800M total invested in Wisconsin shipyard upgrades since 2009",
            "$12M in state tax credits approved to support 400 new jobs",
            "$3M WisDOT harbor grant to dredge Menominee River for larger frigates",
            "Awarded contract to build U.S. Navy Constellation-class frigates in 2020",
            "Awarded contract to build 4 Marine Corps Medium Landing Ships Feb 2026",
            "Part of Great Lakes Shipyard Alliance targeting Coast Guard icebreaker contract"
        ]
    },
    {
        "name": "Brown County, WI",
        "lat": 44.51,
        "lng": -88.01,
        "color": "#1a3d6b",
        "tag": "Active Industry Push",
        "summary": "Opportunity Score: High \n MPZ Status: Strong Candidate",
        "bullets": [
            "Builder of the USCG Response Boat-Medium, a flagship small boat program",
            "Achieved 50% production efficiency through modular assembly line manufacturing",
            "Produces aluminum superstructure panels and modules for Navy Freedom Class LCS",
            "Fincantieri Marine Group HQ support office located in Green Bay metro area",
            "Facility located on the Fox River with climate-controlled workshops and advanced welding tech",
            "Part of Great Lakes Shipyard Alliance targeting Coast Guard icebreaker contract",
            "3,000 total Fincantieri employees across 3 Wisconsin yards"
        ]
    },
    {
        "name": "Door County, WI",
        "lat": 44.8350,
        "lng": -87.3600,
        "color": "#1a3d6b",
        "tag": "Formal MPZ Coalition",
        "summary": "Opportunity Score: High \n MPZ Status: Strong Candidate",
        "bullets": [
            "Fincantieri Bay Shipbuilding is a 63-acre facility with a shipbuilding history dating back to 1918 and is the largest employer in Door County with 887 employees",
            "Fincantieri completed a $300M capital expansion plan that included a new floating drydock and CNC manufacturing equipment",
            "In 2022 the yard launched the MV Mark W. Barker which was the first new Great Lakes freighter built in 40 years",
            "The facility is currently building LNG bunkering barges pioneering clean fuel solutions for Great Lakes commercial shipping",
            "Fincantieri Bay Shipbuilding is the premier repair facility for the entire Great Lakes fleet and operates year round",
            "The yard is a member of the Great Lakes Shipyard Alliance which is actively competing for the Coast Guard icebreaker contract",
            "A $30M shipyard expansion was completed in 2020 to accommodate larger and more complex vessels"
        ]
    },
    {
        "name": "Douglas County, WI",
        "lat": 46.6369,
        "lng": -91.8985,
        "color": "#1a3d6b",
        "tag": "Formal MPZ Coalition",
        "summary": "Opportunity Score: High \n MPZ Status: Strong Candidate",
        "bullets": [
            "Fraser Shipyards has a 125-year history and is one of the oldest industrial employers in the city of Superior, Wisconsin",
            "The facility spans 60 acres on Lake Superior and features heavy-duty dry docks capable of servicing the largest Great Lakes vessels",
            "Fraser Industries secured $40M in financing for a shipyard expansion that is expected to grow full-time employment from 200 to 400 workers.",
            "Fraser Shipyards received a federal MARAD Small Shipyard Grant in 2025 to support workforce development and equipment upgrades",
            "Fraser is a co-founder of the Fourth Coast Shipbuilding Alliance alongside Fincantieri Marine Group and Donjon Marine",
            "The alliance is actively competing for the U.S. Coast Guard contract to build 7 new Homeland Security Cutter light icebreakers",
            "Fraser CEO Patrick Kelly explicitly cited Maritime Prosperity Zones as key to strengthening relationships among regional industry partners",
            "Every direct shipbuilding job at Fraser supports an estimated 2.7 additional contractor jobs in the surrounding region"
        ]
    },
    {
        "name": "Erie County, PA",
        "lat": 42.12,
        "lng": -80.08,
        "color": "#1a3d6b",
        "tag": "Formal MPZ Coalition",
        "summary": "Opportunity Score: High \n MPZ Status: Strong Candidate",
        "bullets": [
            "Donjon Shipbuilding and Repair operates a 44-acre facility on Lake Erie with one of the largest dry docks on the Great Lakes at 1,250 feet by 120 feet",
            "The facility is one of only two dry docks on the Great Lakes capable of servicing 1,000-foot self-unloading vessels",
            "Donjon co-founded the Fourth Coast Shipbuilding Alliance alongside Fincantieri Marine Group and Fraser Shipyards",
            "The alliance submitted a response to the government's request for information for the Coast Guard icebreaker contract for 7 new light icebreakers",
            "Donjon CEO John Witte cited MPZs as critical to expanding domestic industrial capacity on the Great Lakes",
            "Erie Western PA Port Authority Executive Director called the alliance a pivotal moment for Erie and the entire Great Lakes region",
            "A proposed new naval shipyard on the former Erie Coke site could generate 800 to 1,200 direct jobs and 1,360 to 2,040 total jobs in the region",
            "Erie County generated $9.5M in nonemployer marine economy receipts in 2022 — the only Great Lakes county in Pennsylvania"
        ]
    },
    {
        "name": "Porter County, IN",
        "lat": 41.5400,
        "lng": -87.0900,
        "color": "#1a3d6b",
        "tag": "Active Industry Push",
        "summary": "Opportunity Score: High \n MPZ Status: Emerging Candidate",
        "bullets": [
            "Ports of Indiana-Burns Harbor is located in Porter County and generates $4.6 billion in annual economic impact which is the highest of any port in Indiana",
            "The port handles over 2 million tons of cargo per year and hosts more than 30 companies including 15 steel-related businesses and three steel mills",
            "Indiana's maritime industry overall contributes $27 billion in economic revenue and supports 157,000 jobs statewide",
            "A $77M investment package is currently underway at Burns Harbor including a new bulk cargo facility dock rehabilitations and industrial site development",
            "Federal approval was received to build the first container terminal on Lake Michigan at Burns Harbor expected to be operational in 2026",
            "The port has direct access to international markets via the St Lawrence Seaway and connects to 20 states via the inland waterway system",
            "Ports of Indiana CEO Jody Peacock has publicly stated that Indiana is uniquely positioned to lead the next wave of maritime innovation in America",
            "Ports of Indiana is actively in talks with private shipbuilders about establishing a new shipbuilding operation at Burns Harbor",
            "Sen Todd Young has personally advocated to the Trump administration and industry leaders about Burns Harbor as a future shipbuilding site"
        ]
    },
    {
        "name": "Lorain County, OH",
        "lat": 41.4520,
        "lng": -82.1824,
        "color": "#1a3d6b",
        "tag": "Active Industry Push",
        "summary": "Opportunity Score: Medium \n MPZ Status: Emerging Candidate",
        "bullets": [
            "Bartlett Maritime Corporation is based in northeast Ohio and is pursuing a plan to bring submarine maintenance and repair facilities to Lorain and Lordstown",
            "Bartlett Maritime received a $3M contract from BlueForge Alliance in March 2024 to provide a rotational workforce of trained Navy welders",
            "The company has a national labor agreement with the International Brotherhood of Boilermakers to recruit Midwest welders for Navy shipbuilding and repair projects",
            "Bartlett publicly welcomed the April 2025 MPZ executive order and specifically cited northeast Ohio's skilled workforce and industrial development potential",
            "Bartlett's plan proposes an estimated 5000 direct permanent jobs for Ohio through two privately owned companies",
            "The plan leverages Goldman Sachs investment banking and Squire Patton Boggs legal counsel to structure Navy facility lease-purchase financing",
            "Ohio AFL-CIO and local union leaders in Lorain have publicly rallied behind the Bartlett Maritime vision",
            "Proposed facilities include component repair centers in Lorain and Lordstown though no construction has begun as of 2026",
            "Sen Jon Husted (R-OH) co-signed the bipartisan Great Lakes MPZ letter to President Trump"
        ]
    },
    {
        "name": "Cuyahoga County, OH",
        "lat": 41.4993,
        "lng": -81.6944,
        "color": "#1a3d6b",
        "tag": "Active Industry Push",
        "summary": "Opportunity Score: Medium \n MPZ Status: Emerging Candidate",
        "bullets": [
            "The Port of Cleveland is one of the largest ports on the Great Lakes and generates over $7 billion in annual economic activity tied to 23000 jobs",
            "Roughly 13 million tons of cargo move through Cleveland Harbor each year connecting Ohio to global markets via the St Lawrence Seaway",
            "The Cleveland-Cuyahoga County Port Authority was awarded $4.2 million in Ohio Maritime Assistance Program grants in 2026 for dock rehabilitation and harbor resilience projects",
            "The Port has received over $94 million in Clean Ports grants and $105 million in infrastructure investment over the last decade",
            "Great Lakes Shipyard on the Cuyahoga River is a full-service facility offering drydocking fabrication and repair services for government and commercial vessels",
            "The Great Lakes Group operates a 900-ton mobile Travelift and specializes in new construction and maintenance for the Great Lakes fleet",
            "The Cleveland-Cuyahoga County Port Authority has previously used bond financing to attract major employers like Amazon and the same model has been proposed for Navy facility development",
            "Sen Jon Husted (R-OH) co-signed the bipartisan Great Lakes MPZ letter directly citing Ohio's manufacturing capacity and readiness"
        ]
    },
    {
        "name": "Southeast Michigan",
        "lat": 42.4000,
        "lng": -83.1000,
        "color": "#1a3d6b",
        "tag": "Formal MPZ Coalition",
        "summary": "Opportunity Score: High \n MPZ Status: Strong Candidate",
        "bullets": [
            "Southeast Michigan sits at the center of a 30+ organization formal MPZ coalition spanning 4 counties and over 1800 square miles of industrial and maritime infrastructure",
            "Michigan has approximately 300 shipbuilding suppliers already operating statewide with strong concentration in the southeast region",
            "Around 70% of the value of a ship is not generated in the shipyard itself making Southeast Michigan's deep engineering workforce in autonomy control power and propulsion uniquely valuable",
            "The region has 3200 miles of Great Lakes shoreline 33 active ports and direct access to the St Lawrence Seaway and Atlantic Ocean",
            "U-M's naval architecture program has produced 1800+ graduates over 30 years including 800+ doctoral students making it the most productive program of its kind in the country",
            "The $50M Michigan Maritime Manufacturing Initiative with the Navy and DOL is the largest defense workforce investment in Michigan in recent years",
            "An $8M federal Department of Labor grant was awarded in October 2025 specifically to train Michigan workers in welding marine electrical and skilled maritime trades",
            "American shipyards are currently missing an estimated 50% of the necessary workforce and Southeast Michigan is one of the few regions with the engineering talent to close that gap",
            "The SHIPS for America Act calls for 250 new vessels over 10 years and Southeast Michigan's supply chain is already aligned to support that demand"
        ]
    },
    {
        "name": "Cook County, IL",
        "lat": 41.8781,
        "lng": -87.6298,
        "color": "#111111",
        "tag": "Congressional Action",
        "summary": "Opportunity Score: Low \n MPZ Status: Congressional Support Only",
        "bullets": [
            "Sen Tammy Duckworth (D-IL) co-signed the December 2025 bipartisan letter to President Trump urging Great Lakes MPZ designation alongside 7 other senators",
            "The letter specifically called for defining Great Lakes Prosperity Zones by industrial activity and expanding federal investment in workforce training",
            "Illinois has significant port activity through the Port of Chicago and Lake Michigan waterfront but no formal MPZ coalition or active shipbuilding push as of 2026",
            "Cook County is home to over 5 million people and one of the largest manufacturing workforces in the Midwest making it a potential future player if MPZ designation expands regionally",
            "No active shipyard or formal industry coalition has been identified in Cook County at this time"
        ]
    },
    {
        "name": "Dane County, WI",
        "lat": 43.0731,
        "lng": -89.4012,
        "color": "#111111",
        "tag": "Congressional Action",
        "summary": "Opportunity Score: Low \n MPZ Status: Congressional Support Only",
        "bullets": [
            "Sen Tammy Baldwin (D-WI) is one of the lead Senate champions for Great Lakes MPZ designation and co-led the December 2025 bipartisan letter to President Trump alongside Sen Todd Young",
            "Baldwin has also pushed the Navy directly to protect Wisconsin shipbuilding jobs after the Constellation-class frigate cancellation in late 2025",
            "Dane County is home to Madison and the University of Wisconsin system but has no active port shipyard or maritime industry coalition tied to MPZ designation",
            "Baldwin's influence as a senior senator from Wisconsin gives the broader Wisconsin shipbuilding coalition significant political weight in Washington"
        ]
    },
    {
        "name": "Hennepin County, MN",
        "lat": 44.9778,
        "lng": -93.2650,
        "color": "#111111",
        "tag": "Congressional Action",
        "summary": "Opportunity Score: Low \n MPZ Status: Congressional Support Only",
        "bullets": [
            "Sen Amy Klobuchar co-signed the December 2025 bipartisan Great Lakes MPZ letter to President Trump alongside 7 other senators",
            "Hennepin County is home to Minneapolis and has no active port shipyard or maritime industry coalition tied to MPZ designation",
            "Minnesota's historic maritime connection runs through Duluth and the Twin Ports on Lake Superior rather than the Twin Cities metro area",
            "In January 2026 Klobuchar announced she is running for governor of Minnesota which may affect her continued Senate advocacy for Great Lakes shipbuilding"
        ]
    },

    {
        "name": "Galveston County, TX",
        "lat": 29.3013,
        "lng": -94.7977,
        "color": "#1a3d6b",
        "tag": "Active Industry Push",
        "summary": "Opportunity Score: High \n MPZ Status: Strong Candidate",
        "bullets": [
            "Davie Defense acquired Gulf Copper and Manufacturing's shipbuilding assets in Galveston in December 2025 with all required federal approvals including CFIUS clearance",
            "Davie Defense is the US subsidiary of the Inocea Group backed by Davie Shipbuilding in Canada and Helsinki Shipyard in Finland which has built 50% of the world's icebreaker fleet",
            "The planned $1 billion transformation of the historic Gulf Copper facility into an American Icebreaker Factory is projected to create 2400 direct jobs and 7000 statewide",
            "Total projected economic impact of the Davie Defense expansion exceeds $9 billion for the state of Texas",
            "Davie Defense is in active negotiations with the US Coast Guard to deliver 5 Arctic Security Cutters with a promised 26-month delivery timeline from contract signing",
            "In February 2026 Governor Abbott awarded Davie Defense a $21.7M Texas Enterprise Fund grant to support the expansion",
            "Gulf Copper also expanded its agreement with Huntington Ingalls Industries to fabricate structural units for the Navy's Arleigh Burke class destroyers",
            "Galveston College and Gulf Copper launched a shipfitting apprenticeship program in September 2025 to build the local workforce pipeline",
            "Heritage Foundation cited Galveston as a natural choice for MPZ designation given its deep water Gulf access and active icebreaker investment"
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
    {
        "name": "Fincantieri Marinette Marine",
        "lat": 45.0980,
        "lng": -87.6290,
        "type": "industry",
        "role": "World-class Navy shipbuilder, the anchor of Great Lakes Shipyard Alliance"
    },
    {
        "name": "Fincantieri ACE Marine",
        "lat": 44.5133,
        "lng": -88.0165,
        "type": "industry",
        "role": "Aluminum vessel specialist. Coast Guard and Navy supplier, Great Lakes Shipyard Alliance member"
    },
    {
        "name": "Fincantieri Marine Group — GBO",
        "lat": 44.4890,
        "lng": -88.0320,
        "type": "government",
        "role": "US subsidiary HQ support office that runs `logistics and administration for all 3 Wisconsin shipyards"
    },
    {
        "name": "Fincantieri Bay Shipbuilding",
        "lat": 44.8350,
        "lng": -87.3600,
        "type": "industry",
        "role": "Full service Great Lakes shipyard specializing in new construction, repair and conversion. Member of the Great Lakes Shipyard Alliance pursuing Coast Guard icebreaker contract"
    },
    {
        "name": "Fraser Shipyards",
        "lat": 46.7213,
        "lng": -92.0785,
        "type": "industry",
        "role": "125-year-old Great Lakes shipbuilder and co-founder of the Fourth Coast Shipbuilding Alliance. Actively competing for the Coast Guard icebreaker contract and received a federal MARAD grant in 2025"
        },
    {
        "name": "Donjon Shipbuilding and Repair",
        "lat": 42.1350,
        "lng": -80.0780,
        "type": "industry",
        "role": "One of the largest Great Lakes shipyards, co-founder of the Fourth Coast Shipbuilding Alliance and Coast Guard icebreaker bid lead"
    },
    {
        "name": "Erie Western PA Port Authority",
        "lat": 42.1380,
        "lng": -80.0820,
        "type": "government",
        "role": "Port authority and landlord of Donjon Shipbuilding"
    },
    {
        "name": "Ports of Indiana-Burns Harbor",
        "lat": 41.6266,
        "lng": -87.1539,
        "type": "government",
        "role": "State-owned deepwater port on Lake Michigan actively pursuing shipbuilding operations and in talks with private shipbuilders"
    },
    {
        "name": "Cleveland-Cliffs Burns Harbor",
        "lat": 41.6200,
        "lng": -87.1400,
        "type": "industry",
        "role": "Major steel mill producing steel plate used directly in U.S. Navy vessels, one of the largest integrated steel operations on the Great Lakes"
    },
    {
        "name": "Ports of Indiana-Burns Harbor",
        "lat": 41.6266,
        "lng": -87.1539,
        "type": "government",
        "role": "State-owned deepwater port on Lake Michigan generating $4.6B in annual economic impact and actively pursuing new shipbuilding operations"
    },
    {
        "name": "Bartlett Maritime Corporation",
        "lat": 41.4520,
        "lng": -82.1824,
        "type": "industry",
        "role": "Northeast Ohio firm proposing submarine maintenance and repair facilities with a $3M BlueForge Alliance contract for a Navy rotational welder workforce program"
    },
    {
        "name": "Bartlett Maritime Corporation",
        "lat": 41.4520,
        "lng": -82.1824,
        "type": "industry",
        "role": "Northeast Ohio firm proposing submarine maintenance and repair facilities with a $3M BlueForge Alliance contract for a Navy rotational welder workforce program"
    },
    {
        "name": "Port of Cleveland",
        "lat": 41.5090,
        "lng": -81.6930,
        "type": "government",
        "role": "One of the largest Great Lakes ports generating $7B in annual economic activity with active infrastructure investment and bond financing capacity for maritime development"
    },
    {
        "name": "Great Lakes Shipyard",
        "lat": 41.4840,
        "lng": -81.7140,
        "type": "industry",
        "role": "Full service shipyard on the Cuyahoga River specializing in new construction fabrication and repair for commercial and government vessels"
    },
    {
        "name": "University of Wisconsin Madison",
        "lat": 43.0731,
        "lng": -89.4012,
        "type": "academic",
        "role": "Emerging maritime engineering partner with active Fincantieri internship program sending students to Trieste Italy and building research ties to Wisconsin shipyards"
    },
    {
        "name": "Davie Defense / Gulf Copper Shipyard",
        "lat": 29.3100,
        "lng": -94.8200,
        "type": "industry",
        "role": "America's newest specialized shipbuilder targeting Arctic Security Cutter contract with a $1B icebreaker factory investment backed by Canada and Finland"
    },
    {
        "name": "Galveston College",
        "lat": 29.2985,
        "lng": -94.7946,
        "type": "academic",
        "role": "Launched shipfitting apprenticeship program with Gulf Copper in 2025 to build the local maritime workforce pipeline"
    },
    {
        "name": "California Forever / Solano Shipyard",
        "lat": 38.1100,
        "lng": -121.8900,
        "type": "industry",
        "role": "Silicon Valley-backed developer proposing the largest shipyard in the US on a 7500-acre site on the Sacramento River delta targeting uncrewed vessel and naval construction"
    },
    {
        "name": "Mare Island / Nimitz Group",
        "lat": 38.1147,
        "lng": -122.2569,
        "type": "government",
        "role": "Historic naval shipyard site formally included in the California Delta MPZ proposal with active redevelopment plans for maritime manufacturing"
    },
    {
        "name": "Cal Poly Maritime Academy",
        "lat": 38.0965,
        "lng": -122.2607,
        "type": "academic",
        "role": "Formal education and workforce training partner in the California Delta MPZ coalition preparing Coast Guard-licensed deck officers and shipyard operations managers"
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
