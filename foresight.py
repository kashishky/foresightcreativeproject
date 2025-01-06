import folium
from folium.plugins import TimeSliderChoropleth
from folium.features import DivIcon
from folium import Map
from folium.plugins import FloatImage
from branca.element import Html
import pandas as pd
import json


#milestones
milestones = [
    {
        "name": "Rio Grande Valley Health Education Program",
        "coords": [26.2034, -98.2300],
        "date": "2025-08-10",
        "description": "In agricultural communities in the Rio Grande Valley, pesticide exposure is a critical health issue for children, leading to chronic illnesses such as asthma and kidney disease. This program combines bilingual workshops with mobile health units to address these challenges comprehensively. The workshops are conducted in schools and community centers, teaching families how to safely handle pesticides, recognize early symptoms of exposure, and access care. The mobile units, equipped with diagnostic tools, provide health screenings and distribute protective gear, including gloves and masks, to farm workers’ children. High school students are recruited and trained as peer educators, fostering a culture of health advocacy and sustainability within the region.",
        "stakeholders": "The Texas Department of Health funds the initiative and coordinates its public health goals. Local clinics provide follow-up care for children identified during screenings. AHEC Scholars work on capacity building by involving medical students in culturally sensitive health outreach programs.",
        "image": "watercolorrgv.webp"
    },
    {
        "name": "Navajo Nation Environmental Initiative",
        "coords": [36.068, -109.045],
        "date": "2029-03-20",
        "description": "Generations of Navajo children have faced health risks due to uranium contamination in water sources, a legacy of extensive mining operations. This initiative aims to address these issues through a combination of infrastructure improvements and educational programs. It includes the installation of high-efficiency water purification systems in schools and community hubs, ensuring clean water access. Children are engaged through the 'Water Guardians' program, where they learn to test water quality using portable kits, document findings, and present them to local leaders. The initiative integrates Navajo storytelling traditions to teach environmental stewardship and foster pride in cultural heritage.",
        "stakeholders": "The EPA Office of Environmental Justice provides funding and technical expertise for water purification projects. Navajo Nation leaders ensure cultural alignment and community participation. The CDC contributes by monitoring health outcomes, and universities partner to supply educational resources and equipment for the 'Water Guardians' program.",
        "image": "navajo.webp"
    },
        {
        "name": "Urban Child Nutrition Initiative in South Bronx",
        "coords": [40.817, -73.922],
        "date": "2026-11-12",
        "description": "In the South Bronx, where food insecurity is a persistent issue, this program transforms school rooftops into thriving urban farms. These farms grow fresh vegetables and herbs, which are incorporated into school lunches and distributed to families in need. Children participate in planting, harvesting, and cooking workshops, learning not just about nutrition but also about urban sustainability and farming. Additionally, the program organizes 'Farm to Table Fridays,' where students cook and share meals with their families using produce they helped grow. A complementary curriculum on food justice and climate change ensures students understand the broader context of their work.",
        "stakeholders": "The New York Department of Education funds the construction of rooftop farms and provides logistical support for school lunches. Local chefs volunteer for cooking workshops, and community nonprofits help distribute surplus produce to food-insecure families.",
        "image": "southbronx.webp"
    },
    {
        "name": "Hawaiian Youth Environmental Education",
        "coords": [19.8968, -155.5828],
        "date": "2033-06-15",
        "description": "Hawaii's unique ecosystems are under threat from climate change, including rising sea levels and habitat destruction. This program creates immersive 'Living Classrooms' on beaches and in forests, where children learn to preserve their environment through hands-on conservation activities. Students work on coral reef restoration, plant native trees in degraded areas, and design rain gardens to prevent soil erosion. The program also incorporates cultural elements, such as traditional Hawaiian ecological knowledge and chants, to connect children to their heritage while teaching sustainability. A key highlight is the annual 'Climate Action Festival,' where children showcase their projects and propose innovative solutions to local leaders.",
        "stakeholders": "The Hawaiian Department of Education integrates the program into school curricula, ensuring broad participation. Conservation organizations provide resources for fieldwork, and community leaders guide the integration of traditional knowledge. Local businesses sponsor the festival to amplify its impact.",
        "image": "https://www.wildhawaii.org/wp-content/uploads/2020/08/9-keiki-education-hawaii-wildlife-fund-header.jpg"
    },
    {
        "name": "Youth Mental Health Clinics in Appalachia",
        "coords": [37.4316, -78.6569],
        "date": "2027-04-25",
        "description": "Mental health challenges in Appalachia, driven by economic stress and the opioid epidemic, affect thousands of children. This initiative creates school-based clinics offering free mental health services, including one-on-one counseling, group therapy, and family support sessions. The clinics also run mentorship programs, pairing children with trained mentors who provide guidance on coping strategies and career aspirations. To reduce stigma around mental health, the program hosts public events featuring testimonies from local leaders and workshops on trauma-informed care for teachers and parents. The initiative leverages telemedicine to ensure rural students have consistent access to licensed therapists.",
        "stakeholders": "The National Institutes of Mental Health funds clinic operations and telemedicine infrastructure. Local nonprofits provide trained counselors, and school districts offer space and coordinate outreach efforts with families.",
        "image": "https://media.npr.org/assets/img/2021/08/25/HarveySutton-52e9a0a7321826a1cc1da02f759f3a27433cc720.jpg"
    },
    {
        "name": "Tennessee Children's Climate Adaptation Network",
        "coords": [35.5175, -86.5804],  # central tennessee
        "date": "2038-02-14",
        "description": "Frequent flooding in Tennessee disrupts education, damages infrastructure, and poses significant risks to children. This network fosters collaboration between schools, local governments, and families to build climate resilience among children. It establishes multi-functional 'Resilience Hubs' that serve as schools during normal times and safe shelters during emergencies. Equipped with solar-powered generators, elevated classrooms, and emergency supplies, these hubs are designed to withstand extreme weather events. Students play an active role by designing and implementing rain gardens, which double as flood mitigation systems and outdoor learning spaces. The network also offers workshops on emergency preparedness, teaching children essential survival skills such as evacuation planning and first aid. Community outreach efforts include flood response drills, ensuring families are well-prepared during crises.",
        "stakeholders": "The Tennessee Emergency Management Agency funds infrastructure upgrades and disaster preparedness training. Local architects and engineers work with schools to design climate-resilient buildings. Nonprofits specializing in disaster relief provide educational resources and community engagement support, while local governments ensure equitable resource distribution across flood-prone regions.",
        "image": "https://images.squarespace-cdn.com/content/v1/63613c7b0a0c3071cdfbbfa0/3a0b1ae3-1518-4428-92ca-80788bafab00/Outdoor+education+sessiion.jpg"
    },
    {
        "name": "California Wildfire Safety Education",
        "coords": [36.7783, -119.4179],
        "date": "2025-10-18",
        "description": "With wildfires becoming increasingly common in California, this program teaches children how to prepare for and respond to fire emergencies. Interactive workshops cover topics such as creating defensible space around homes, emergency evacuation protocols, and basic first aid for burns and smoke inhalation. The program also integrates fire ecology lessons, helping students understand the role of wildfires in maintaining certain ecosystems. As part of the initiative, children collaborate with local fire departments to create fire prevention murals and safety posters displayed throughout their communities.",
        "stakeholders": "Cal Fire offers fire safety training and educational materials. The California Department of Education ensures the program aligns with state standards, and local artists assist children in creating impactful safety visuals.",
        "image": "https://www.easternmennonite.org/wp-content/uploads/2021/03/IMG_3171-scaled.jpg"
    },
    {
        "name": "Florida Mangrove Guardians Program",
        "coords": [27.9944024, -81.7602544],
        "date": "2034-08-10",
        "description": "Coastal erosion and storm surges in Florida threaten both the environment and children’s safety. This program trains students as 'Mangrove Guardians,' equipping them to plant and maintain mangroves along vulnerable shorelines. Hands-on activities include designing protective barriers using mangrove saplings and learning about their ecological benefits in preventing erosion and protecting biodiversity. Virtual reality (VR) simulations allow children to visualize the role of mangroves during storms, deepening their understanding. Additionally, the program organizes public planting events, where families can join their children in creating a stronger coastal defense.",
        "stakeholders": "The Florida Department of Environmental Protection funds planting initiatives and provides technical guidance. Local universities develop VR simulations, and community groups facilitate family participation in planting events.",
        "image": "https://natureconservancy-h.assetsadobe.com/is/image/content/dam/tnc/nature/en/photos/m/a/Mangrove_Planting_Rachel_Hancock_Davis_IMG_2280.jpg?crop=0%2C3%2C3024%2C2008&wid=828&hei=550&scl=3.652173913043478"
    },
    {
        "name": "Chicago Urban Green Spaces for Children",
        "coords": [41.8781, -87.6298],
        "date": "2026-05-14",
        "description": "Limited access to green spaces negatively impacts the mental and physical health of children in low-income Chicago neighborhoods. This program converts vacant lots into community parks featuring playgrounds, gardens, and outdoor classrooms. Children participate in park planning and planting, gaining hands-on experience in urban ecology. The parks also host weekly wellness activities, such as yoga, art therapy, and mindfulness sessions, aimed at reducing stress and promoting emotional well-being.",
        "stakeholders": "The Chicago Parks District leads the construction and maintenance of parks. Local schools organize student participation, and community organizations coordinate wellness activities and outreach efforts.",
        "image": "https://moss-design.com/wp-content/uploads/2014/08/merryman-park.jpg"
    },
    {
        "name": "Detroit Renewable Energy STEM Labs",
        "coords": [42.3314, -83.0458],
        "date": "2032-03-11",
        "description": "Detroit's youth are introduced to renewable energy solutions through school-based STEM labs focusing on wind, solar, and geothermal technologies. These labs provide students with hands-on opportunities to design small-scale renewable energy projects, such as solar-powered water heaters and wind turbines for community use. Partnering with local energy companies, the program also incorporates career mentorship sessions and site visits to renewable energy facilities.",
        "stakeholders": "Detroit Public Schools funds the labs, while renewable energy companies provide materials and mentorship. Local engineers volunteer to guide students through project development.",
        "image": "https://www.freep.com/gcdn/presto/2023/03/24/PDTF/04cedab7-0bfd-4088-a528-96bbbad84820-EcotekLab_030823_16_MW.jpg?width=660&height=430&fit=crop&format=pjpg&auto=webp"
    },
    {
        "name": "Water Preservation in Great Lakes Region",
        "coords": [43.70011, -79.4163],
        "date": "2030-09-29",
        "description": "Water scarcity and pollution in the Great Lakes threaten one of the world's largest freshwater ecosystems. This effort focuses on equipping children with tools and knowledge to become active stewards of water resources. Through school-based workshops, students learn about water testing, filtration techniques, and pollution prevention methods. A key feature is the 'Adopt a Waterway' initiative, where students partner with local conservation groups to clean and monitor streams feeding into the lakes. They also participate in advocacy campaigns, petitioning for stricter pollution controls and community water conservation practices. Children use interactive tools like virtual water cycle simulations and community science apps to track progress and share findings.",
        "stakeholders": "The EPA funds educational resources and community science initiatives. The Great Lakes Commission facilitates connections between schools and conservation groups. Local governments contribute to stream cleanup efforts, and tech companies supply the interactive tools used by students.",
        "image": "https://d2j02ha532z66v.cloudfront.net/wp-content/uploads/2020/05/watershed-kids-activity.jpg"
    },
    {
        "name": "Texas Heatwave Safety in Schools",
        "coords": [31.9686, -99.9018],
        "date": "2028-04-15",
        "description": "With heatwaves intensifying across Texas, children face growing risks of heat-related illnesses. This strategy introduces heat safety measures into school systems, ensuring safer environments for learning and play. Schools are equipped with shaded outdoor areas, hydration stations, and reflective roofing to lower indoor temperatures. Students engage in 'Heat Health' workshops where they learn to recognize signs of dehydration and heat exhaustion, both for themselves and their peers. The initiative also includes creating school-based cooling centers that serve as community hubs during extreme weather events. Families are provided with heat survival kits containing portable fans, electrolyte solutions, and educational materials on staying safe during heatwaves.",
        "stakeholders": "The Texas Department of Health funds infrastructure upgrades and survival kits. Local NGOs organize workshops and distribute resources, while architects and engineers design cooling-focused modifications to school facilities.",
        "image": "https://dmn-dallas-news-prod.cdn.arcpublishing.com/resizer/v2/OOHSEZ3XAFBCDERB7T5J4KZHA4.jpg?auth=1f0a432f5ef06682a9c034448dd33bf50c0542b6851975d6b47f7cdc829bf0a1&height=553&width=830&smart=true&quality=80"
    },
    {
        "name": "NYC Air Quality Awareness and Action",
        "coords": [40.7128, -74.0060],
        "date": "2029-10-11",
        "description": "Air pollution disproportionately affects children in New York City, leading to respiratory issues like asthma and reduced lung development. This city-wide initiative focuses on teaching children about air quality and empowering them to take action. Schools integrate air monitoring devices into science classes, enabling students to measure pollution levels in their neighborhoods. This data is shared with city planners to advocate for cleaner transportation systems and expanded green spaces. Art and storytelling workshops allow children to express the impact of air quality on their lives, creating compelling narratives to raise public awareness. The program also works with local governments to enforce 'clean commute zones' near schools, reducing vehicle emissions.",
        "stakeholders": "The NYC Department of Education integrates air quality monitoring into curricula. Advocacy groups guide students in using data to influence policy changes. Local businesses and community organizations help fund green space projects and support clean commute initiatives.",
        "image": "https://www.the74million.org/wp-content/uploads/2020/08/GettyImages-1224851545-1.jpg"
    },
    {
        "name": "Arizona Desert Resilience",
        "coords": [34.0489, -111.0937],
        "date": "2031-06-30",
        "description": "Arizona’s arid climate poses unique challenges for children, including extreme heat and limited water resources. This initiative immerses students in survival and resilience training, teaching them practical skills such as water conservation, heat management, and sustainable desert living. Activities include designing water-efficient gardens at schools, building solar-powered hydration stations, and learning how to navigate desert terrain safely. The project culminates in an annual 'Desert Resilience Challenge,' where students showcase their knowledge and compete in building sustainable cooling and hydration systems. Workshops also highlight indigenous water-saving techniques, connecting children to local cultural practices.",
        "stakeholders": "The Arizona Department of Education provides funding and curriculum integration. Local NGOs contribute expertise in water conservation, and indigenous leaders share traditional knowledge. Solar energy companies sponsor the design and installation of hydration stations.",
        "image": "https://wateruseitwisely.com/wp-content/uploads/2023/11/IMG_5381-scaled-e1700616505680.jpg"
    },
    {
        "name": "Seattle Youth Climate Innovation Lab",
        "coords": [47.6062, -122.3321],
        "date": "2026-11-21",
        "description": "Seattle's youth play a pivotal role in tackling climate challenges through this hands-on innovation lab. Students collaborate with scientists, engineers, and local leaders to develop creative solutions to mitigate climate impacts in their city. Projects include designing rain gardens to manage urban flooding, building solar-powered bike charging stations, and crafting public awareness campaigns about sustainable lifestyles. Regular 'Climate Action Hackathons' engage students in rapid prototyping of green technologies, such as low-cost air filtration systems for wildfire smoke. The lab also serves as a hub for environmental storytelling, where students use digital media to amplify their message to broader audiences.",
        "stakeholders": "The Washington State Department of Ecology funds lab operations and mentorship programs. Local schools provide facilities and organize hackathons. Environmental nonprofits connect students to real-world projects, and media companies assist with storytelling efforts.",
        "image": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5OnhFGcwfMsCTEMH2iHm4H2PyW7orrKB7eGfDQSV_QSi1tRlRhIh7WqGSoEyFAuSSz9p9okTFclhSDJK0t0fFNs8fA4SNK59hab7SyXbzLe1NrvCEbczdc4UxfAdWZEwnEagvxtyu0Q8/s1600/DSC01882.JPG"
    },
    {
        "name": "Puerto Rico Community Ambassadors",
        "coords": [18.2208, -66.5901],
        "date": "2025-22",
        "description": "Puerto Rico faces recurring hurricanes that severely impact infrastructure and communities, leaving children particularly vulnerable. This initiative focuses on educating and equipping children to be resilience ambassadors within their schools and neighborhoods. Participants attend interactive workshops on disaster preparedness, learning skills such as assembling emergency kits, understanding evacuation procedures, and supporting mental health recovery in peers. Through art and storytelling sessions, children create posters, videos, and social media content to raise community awareness about hurricane safety. Schools also organize 'Safe Space Drills,' where students help identify areas in their neighborhoods that can serve as safe zones during storms. A final community-wide resilience fair showcases these efforts, providing families with resources and connecting them to local disaster response agencies.",
        "stakeholders": "The Puerto Rico Department of Emergency Management provides disaster preparedness training and resources. NGOs contribute materials for emergency kits and lead mental health recovery workshops. Local governments collaborate to designate and upgrade neighborhood safe zones, while schools organize workshops and community fairs.",
        "image": "https://epe.brightspotcdn.com/e4/f9/73706f19935bd81cc4af4ad9a43e/10-puerto-rico-read-aloud-01-story.jpg"
    },
    {
        "name": "Great Plains Climate Agriculture Initiative",
        "coords": [41.4925, -99.9018],
        "date": "2036-09-01",
        "description": "To prepare Great Plains children for a future shaped by climate challenges, this program integrates climate-resilient farming techniques into school curricula. Students learn about water-efficient irrigation, soil regeneration, and sustainable crop rotations through hands-on experiments in school gardens. The initiative culminates in an annual 'Future Farmers Forum,' where children share innovative agricultural solutions.",
        "stakeholders": "Local agricultural extension offices provide resources and mentorship, while state governments fund school garden projects. Universities collaborate to develop educational content.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCRqGdCiv7HIWsaxXoo67Og1bUtxOBmon93g&s"
    },
    {
        "name": "New Orleans Wetlands Restoration",
        "coords": [29.9511, -90.0715],
        "date": "2031-05-10",
        "description": "Wetlands near New Orleans are rapidly disappearing, threatening biodiversity and increasing flood risks. This program engages children in restoring local wetlands by planting marsh grasses and monitoring water quality. Students work alongside ecologists to study the role of wetlands in protecting communities from hurricanes. The program also includes field trips to preserved wetlands and educational workshops on environmental justice.",
        "stakeholders": "Louisiana Department of Wildlife and Fisheries funds restoration activities. Local environmental organizations provide expertise, and schools incorporate workshops into science classes.",
        "image": "https://images.squarespace-cdn.com/content/v1/549815dde4b08b1b04477bfa/1661367728589-6R6O4HG4LZKUZWUYT01S/Canoeing+in+City+Park+4.jpg"
    },
    {
        "name": "Alaska Arctic Research Expedition",
        "coords": [64.2008, -149.4937],
        "date": "2039-01-20",
        "description": "In Alaska, students join researchers on expeditions to study Arctic ecosystems affected by climate change. Children collect data on permafrost melting, polar bear migration patterns, and ice shelf deterioration using cutting-edge technology. The program connects indigenous knowledge with scientific practices, empowering students to address environmental changes in their communities.",
        "stakeholders": "Indigenous tribal councils lead cultural integration efforts. Universities provide equipment and training, while state governments fund logistical support.",
        "image": "https://ua.vps03.fwstatic.download/media/1599961/reu-pep-500x375.jpg?width=500&height=375"
    },
        {
        "name": "Idaho Future Farmers Innovation Hub",
        "coords": [44.0682, -114.7420],
        "date": "2035-04-17",
        "description": "In Idaho's rural communities, children are often disconnected from innovations in agriculture despite living in a farming-dominated region. This innovation hub introduces students to cutting-edge agricultural technologies, such as drones for crop monitoring, soil sensors, and vertical farming techniques. Schools partner with local agricultural businesses to host hands-on workshops, where students prototype solutions for challenges like water shortages and pest management. A key component of the hub is the 'Tech on the Farm' competition, where participants present projects like automated irrigation systems or eco-friendly pest repellents. Winning ideas are piloted on local farms, creating tangible community benefits.",
        "stakeholders": "Idaho State University contributes technical expertise and equipment. Local farmers provide test sites and mentorship, and agricultural tech companies sponsor the competition and supply materials.",
        "image": "https://www.growidahoffa.org/wp-content/uploads/2022/03/jacket-image_7.jpg"
    },
    {
        "name": "Wyoming Adventure Academy",
        "coords": [43.07597, -107.29028],
        "date": "2037-07-10",
        "description": "Wyoming’s rugged landscapes are an ideal classroom for developing leadership and problem-solving skills. The Adventure Academy immerses students in multi-day expeditions where they tackle real-world challenges like building sustainable campsites, tracking wildlife migration, and conducting water quality tests in remote streams. The academy also includes a 'Conservation Solutions Workshop,' where students work in teams to propose actionable strategies for protecting the state’s natural resources. Projects range from improving trail sustainability to designing educational outreach for tourists. These experiences not only cultivate practical skills but also foster a deep connection to Wyoming’s unique environment.",
        "stakeholders": "The National Park Service provides access to protected areas and ecological expertise. Outdoor adventure companies sponsor equipment and guides, while local conservation organizations mentor students in project development.",
        "image": "https://i0.wp.com/www.whatsupwyoming.com/wp-content/uploads/2019/06/ElmLights4.jpg?resize=1021%2C580&ssl=1"
    },
    {
        "name": "Montana Renewable Energy Pioneer Challenge",
        "coords": [46.8797, -110.3626],
        "date": "2034-09-15",
        "description": "Montana's rich energy landscape, from hydroelectric dams to emerging wind farms, presents a unique opportunity for students to explore sustainable power solutions. The Pioneer Challenge invites middle and high school students to design innovative energy systems, such as solar-powered irrigation for community gardens or wind-driven water purifiers. Participants collaborate with local engineers to refine their designs and build working prototypes. The challenge culminates in a state-wide exhibition where students present their projects to energy companies and policymakers, influencing future renewable energy initiatives in Montana.",
        "stakeholders": "The Montana Energy Office funds the challenge and provides technical support. Renewable energy firms supply materials and mentorship, while local governments sponsor the exhibition and consider student proposals for community implementation.",
        "image": "https://montanarenewables.org/wp-content/uploads/2019/09/24A9366-1-200x300.jpg"
    },
    {
        "name": "Utah Desert Guardians Program",
        "coords": [39.32098, -111.09373],
        "date": "2032-03-24",
        "description": "Utah’s arid ecosystems face mounting pressures from climate change and human expansion. The Desert Guardians initiative empowers students to become stewards of their environment through hands-on ecological restoration and cutting-edge conservation technology. Students work on restoring native habitats by planting drought-resistant species and constructing erosion barriers. Using advanced tools like camera traps and water monitoring sensors, participants collect data to assess the health of local ecosystems. These findings are presented at community events, encouraging broader environmental awareness. Special workshops, led by indigenous leaders, teach children traditional water conservation methods adapted to desert climates.",
        "stakeholders": "The Utah Department of Natural Resources funds restoration projects and provides monitoring equipment. Conservation groups offer technical guidance, and indigenous leaders share cultural knowledge about sustainable practices.",
        "image": "https://www.deseret.com/resizer/v2/7H7LEJNQCHQEBJE7NI2AS73OWA.jpg?auth=1d39dd57664b4b3519ea2418ff886b5bb50018bf70996901515b4d5887e41523&focal=1500%2C1008&width=800&height=537"
    },
    {
        "name": "Oregon Wildfire Ecosystem Recovery Initiative",
        "coords": [43.8041, -120.5542],
        "date": "2036-06-12",
        "description": "Oregon’s escalating wildfire crises demand creative solutions for protecting communities and ecosystems. This recovery initiative involves students in rebuilding efforts after wildfires, including planting fire-resistant tree species, constructing erosion control barriers, and studying soil regeneration processes. The program emphasizes fire ecology, teaching children about the role of controlled burns in maintaining healthy forests. Students also assist in developing community wildfire defense plans by mapping fire-prone areas and proposing mitigation strategies like buffer zones and fire breaks. Interactive 'Firefighter for a Day' events allow participants to experience firefighting techniques, fostering respect for emergency responders.",
        "stakeholders": "The Oregon Department of Forestry leads restoration activities and training sessions. Local fire departments collaborate on outreach, and indigenous groups contribute expertise on traditional fire management practices.",
        "image": "https://ashland.news/wp-content/uploads/2024/05/wildfire-education-kids-from-phoenix.jpg"
    },
    {
        "name": "North Dakota Prairie Conservation Corps",
        "coords": [46.7296, -94.6859],
        "date": "2039-08-01",
        "description": "North Dakota’s prairies are home to diverse ecosystems, but they face threats from invasive species and agricultural expansion. The Prairie Conservation Corps engages students in safeguarding these landscapes through restoration projects like planting native grasses, creating pollinator habitats, and mapping invasive species using drone technology. Participants attend workshops on prairie ecology and climate change impacts, preparing them to take on leadership roles in community conservation. The program culminates in a 'Prairie Day Festival,' where children showcase their work through educational booths, interactive demonstrations, and guided tours of restored grasslands.",
        "stakeholders": "North Dakota State University provides ecological expertise and research tools. Conservation organizations fund restoration projects, while local farmers collaborate on land management strategies to balance conservation and agriculture.",
        "image": "https://cdn.forumcomm.com/dims4/default/5416f44/2147483647/strip/true/crop/3024x2016+0+1008/resize/840x560!/quality/90/?url=https%3A%2F%2Fforum-communications-production-web.s3.us-west-2.amazonaws.com%2Fbrightspot%2F57%2F07%2F1a1d8655458b9f38cd02fad196e9%2Fimg-8252.jpg"
    },
        {
        "name": "Kansas Wind and Solar Lab",
        "coords": [38.5003, -98.5006],
        "date": "2032-09-15",
        "description": "Kansas’s wide-open prairies make it a prime location for renewable energy projects. This lab introduces children to wind and solar power through hands-on experimentation and community-based projects. Students design and install small-scale solar arrays and wind turbines to power irrigation systems and school greenhouses. These installations provide clean energy while demonstrating how renewable power can address local challenges. Students also explore energy storage solutions, creating prototypes like battery-powered farm equipment. A regional 'Renewable Futures Expo' highlights their work, connecting them with renewable energy professionals and policymakers.",
        "stakeholders": "Kansas State University provides engineering support and materials. Renewable energy companies sponsor equipment and mentor students. Local governments incorporate successful student projects into broader sustainability plans.",
        "image": "https://i.ytimg.com/vi/oruitJJXWhM/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgSShEMA8=&rs=AOn4CLCJuZJeyR21dcqH006ki6w5Lc6PBQ"
    },
    {
        "name": "Oklahoma Indigenous Land Stewardship Camp",
        "coords": [35.0078, -97.0929],
        "date": "2037-06-10",
        "description": "Oklahoma’s rich cultural heritage and diverse ecosystems create opportunities for children to learn about land stewardship through indigenous knowledge. This summer camp, held on tribal lands, immerses children in traditional ecological practices like controlled burns, natural resource harvesting, and soil restoration techniques. Campers participate in storytelling sessions where tribal leaders share the history of their relationship with the land, fostering a deeper cultural understanding. Projects include restoring riparian zones along rivers and building seed banks to preserve native plant species. Each camper creates a personalized stewardship plan to implement in their local community, ensuring the camp’s lessons have a lasting impact.",
        "stakeholders": "Tribal councils lead the camp activities and provide cultural knowledge. The Oklahoma Department of Wildlife Conservation funds restoration projects. Local schools partner to identify student participants and integrate lessons into broader environmental curricula.",
        "image": "https://osagenews.org/wp-content/uploads/2021/12/osage-youth-win-big-at-oklahoma-native-american-youth-language-fair_61abf981599ae.jpeg"
    }
]


#m map centered on the us with the watercolor theme
m = folium.Map(
    location=[37.8, -96.9],
    zoom_start=3,
    tiles="https://watercolormaps.collection.cooperhewitt.org/tile/watercolor/{z}/{x}/{y}.jpg",
    attr=("Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under CC BY SA.")
    )

citations = [
    "Restore Your Coast. (n.d.). Hawaii. Restore Your Coast.",
    "Schwartz, J. (2021, August 25). 5-year-old hikes Appalachian Trail: Harvey Sutton. NPR.",
    "TCD Type 1. (n.d.). Outdoor education for diabetes awareness. TCD Type 1.",
    "Eastern Mennonite University. (2021, February). Students add wildfire mural to gym. EMU News.",
    "The Nature Conservancy. (n.d.). Why mangroves are important. The Nature Conservancy.",
    "Moss Design. (n.d.). Chicago parks. Moss Design.",
    "Detroit Free Press. (2023, March 24). Ecotek Lab invests in Detroit’s youth, carving a scientific pathway to innovation and success. Detroit Free Press.",
    "Great Lakes Now. (2020, May). Watershed kids activity. Great Lakes Now.",
    "The Dallas Morning News. (2024, August 19). North Texas swelters in heat: How many 100-degree days? When will it cool down? The Dallas Morning News.",
    "The 74 Million. (2020). Best education articles of 2020: Our 20 most popular stories about students, remote schooling, COVID learning loss this year. The 74 Million.",
    "Environmental Exchange. (2023, November). Our presentations. EE Exchange.",
    "Woodland Park Zoo. (2017, August 28). Seattle Youth Climate Action Network: Inspiring the next generation. Zoo Blog.",
    "Education Week. (2017, October). At Puerto Rican school, lifting spirits with read-aloud event. Education Week.",
    "USDA National Institute of Food and Agriculture. (n.d.). News. USDA NIFA.",
    "LOOP NOLA. (n.d.). Canoe trips. LOOP NOLA.",
    "University of the Arctic. (2019, September). Fostering the next generation of Arctic researchers and managers. UArctic News.",
    "The Big E. (2024, September). Say hi to a farmer: Conversations create needed connection at the Big E. MassLive.",
    "Wyoming Kids Environmental Progress. (2019, June). Wyoming's kids make plans for environmental progress. What's Up Wyoming?.",
    "Montana Renewables. (n.d.). Renewable energy activities for kids. Montana Renewables.",
    "Deseret News. (n.d.). Could Utah children help shape the destiny of the ailing Great Salt Lake? Deseret News.",
    "Ashland News. (n.d.). ScienceWorks hosts Sparking Action Community Wildfire Education Day. Ashland News.",
    "Mitchell Republic. (n.d.). South Dakota youth participate in rangeland and soils education. Mitchell Republic.",
    "Salina Post. (n.d.). Kansas’s renewable energy initiatives. Salina Post.",
    "Osage News. (n.d.). Osage youth win big at Oklahoma Native American Youth Language Fair. Osage News."
]


#markers with popups
for idx, milestone in enumerate(milestones):
    #skip the first three milestones as they dont have citations
    if idx < 3:
        citation_text = "Source: Custom Illustration"
    else:
        citation_text = f"Source: {citations[idx-3]}"    
    popup_content = f"""
        <div style='max-width: 800px; font-size: 14px; font-family: Open Sans, sans-serif; text-align: left; display: flex; align-items: center;'>
            <!-- Left Sction: Descrip and Stakeholders -->
            <div style='flex: 1; padding-right: 20px;'>
                <!-- Milestone Name -->
                <strong style='font-size: 18px; font-weight: bold; line-height: 1.8;'>{milestone['name']}</strong>
                <!-- Descrip -->
                <p style='line-height: 1.5; margin-top: 10px;'>{milestone['description']}</p>
                <!-- Stakeholders -->
                <strong>Stakeholders:</strong> <span>{milestone['stakeholders']}</span>
            </div>
            
            <!-- Right Section: Image with Superimposed Date -->
            <div style='flex: 0 0 40%; position: relative; text-align: center;'>
                <img src="{milestone['image']}" alt="{milestone['name']} Illustration"
                    style="width: 100%; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);">
                 <!-- citation -->
                <div style='margin-top: 10px; font-size: 10px; font-style: italic; align-items: left'>
                {citation_text}
                </div>
                <!-- Date in Top-Right Corner -->
                <div style='position: absolute; top: 10px; right: 10px; 
                            font-size: 30px; font-style: italic; font-family: Montserrat, sans-serif; font-weight: bold; color: #1cabe2; background-color: white; padding: 0 2px'>
                    {milestone['date'].replace("-", ".")}
                </div>
            </div>
        </div>
    """
    folium.Marker(
        location=milestone["coords"],
        popup=folium.Popup(popup_content, max_width=800),
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

#thought bubble HTML and CSS
thought_bubble_html = """
<div id="thought-bubble" style="
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 300px;
    background-color: #f0f8ff;
    color: #333;
    font-family: Arial, sans-serif;
    font-size: 14px;
    line-height: 1.6;
    padding: 15px;
    border: 2px dashed #1cabe2;
    border-radius: 15px;
    box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2);
    z-index: 1000;
">
    <strong>Vision for the Future:</strong><br>
    Each initiative contributes to a broader 20-year plan, building upon existing work and addressing ongoing challenges faced by children across the U.S.<br><br>
    These projects begin by introducing the current challenge and propose integrated interventions to improve well-being, leveraging the strengths of communities, policies, and innovation.<br><br>
    <em>Together, they aim to secure a brighter, healthier future for children and youth in the United States.</em>
</div>
"""

#inject the HTML into the map
bubble_element = Html(thought_bubble_html, script=True)
m.get_root().html.add_child(bubble_element)


#save the map
m.save("interactive_story_map.html")
