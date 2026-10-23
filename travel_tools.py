"""Shared travel tools for the Wayvora AI demo.

All attraction data in this module is illustrative sample data, not live inventory.
Add destinations to DESTINATIONS to make them available in the app dropdown.
"""
from __future__ import annotations

DESTINATIONS = {
    "jaipur": [
        {"name": "Amber Fort", "type": "history", "entry": 500, "duration": "2–3 hours", "time": "Morning", "description": "Give yourself time for the courtyards and hilltop views."},
        {"name": "Hawa Mahal", "type": "history", "entry": 200, "duration": "1 hour", "time": "Morning", "description": "A compact stop for the famous pink facade and its intricate windows."},
        {"name": "City Palace", "type": "culture", "entry": 400, "duration": "2 hours", "time": "Afternoon", "description": "Slow down and look closely at royal-era details."},
        {"name": "Jantar Mantar", "type": "culture", "entry": 200, "duration": "1–2 hours", "time": "Afternoon", "description": "An open-air collection of historic astronomical instruments."},
        {"name": "Johari Bazaar", "type": "shopping", "entry": 0, "duration": "1–2 hours", "time": "Evening", "description": "Wander the lanes, compare stalls, and leave room to browse."},
        {"name": "Jal Mahal viewpoint", "type": "nature", "entry": 0, "duration": "45 minutes", "time": "Sunset", "description": "A short lakeside pause for views across the water."},
        {"name": "Central Park", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "An easy green-space break between busier sightseeing stops."},
        {"name": "Local food walk", "type": "food", "entry": 500, "duration": "2 hours", "time": "Evening", "description": "Use this as a flexible window to sample local snacks and sweets."},
    ],
    "delhi": [
        {"name": "Humayun's Tomb", "type": "history", "entry": 400, "duration": "2 hours", "time": "Morning", "description": "A garden-tomb complex worth exploring at an unhurried pace."},
        {"name": "India Gate", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Evening", "description": "An outdoor landmark stop, especially suited to an evening walk."},
        {"name": "National Museum", "type": "culture", "entry": 300, "duration": "2 hours", "time": "Afternoon", "description": "Choose a few galleries that interest you rather than rushing through."},
        {"name": "Qutub Minar", "type": "history", "entry": 400, "duration": "2 hours", "time": "Morning", "description": "Explore the minaret and the surrounding historic complex."},
        {"name": "Chandni Chowk", "type": "food", "entry": 0, "duration": "2 hours", "time": "Evening", "description": "A lively area for food stops and a look at Old Delhi street life."},
        {"name": "Lodhi Garden", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "A leafy walk with historic tombs tucked among the paths."},
        {"name": "Dilli Haat", "type": "shopping", "entry": 100, "duration": "2 hours", "time": "Afternoon", "description": "Browse craft stalls and food counters; offerings vary by stall."},
    ],
    "goa": [
        {"name": "Fontainhas", "type": "culture", "entry": 0, "duration": "1–2 hours", "time": "Morning", "description": "Take a gentle walk through the Latin Quarter's colorful streets."},
        {"name": "Basilica of Bom Jesus", "type": "history", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "A historic church visit; check service times and visitor guidance."},
        {"name": "Dona Paula viewpoint", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Sunset", "description": "A breezy viewpoint to pause and look out over the water."},
        {"name": "Candolim Beach", "type": "nature", "entry": 0, "duration": "2 hours", "time": "Evening", "description": "Keep the evening open for a beach walk and an unhurried meal."},
        {"name": "Anjuna market area", "type": "shopping", "entry": 0, "duration": "2 hours", "time": "Afternoon", "description": "Browse local shops and market stalls; check market days first."},
        {"name": "Goan food walk", "type": "food", "entry": 600, "duration": "2 hours", "time": "Evening", "description": "Leave room to try regional dishes at a few different places."},
        {"name": "Spice plantation visit", "type": "nature", "entry": 900, "duration": "3 hours", "time": "Morning", "description": "A longer countryside outing; confirm transport and visit details first."},
    ],
    "mumbai": [
        {"name": "Gateway of India", "type": "history", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "Start by the waterfront and take in the landmark at an easy pace."},
        {"name": "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya", "type": "culture", "entry": 200, "duration": "2 hours", "time": "Morning", "description": "Choose a few galleries rather than trying to cover everything."},
        {"name": "Marine Drive", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Sunset", "description": "A classic promenade for a walk and sea views."},
        {"name": "Colaba Causeway", "type": "shopping", "entry": 0, "duration": "1–2 hours", "time": "Afternoon", "description": "Browse small shops and street stalls; compare before buying."},
        {"name": "Crawford Market area", "type": "shopping", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "A busy market area for everyday city scenes and browsing."},
        {"name": "Mumbai street-food stop", "type": "food", "entry": 400, "duration": "1–2 hours", "time": "Evening", "description": "Try local favorites from busy, well-reviewed vendors."},
    ],
    "agra": [
        {"name": "Taj Mahal", "type": "history", "entry": 1100, "duration": "2–3 hours", "time": "Morning", "description": "Arrive early and allow time for security and the gardens."},
        {"name": "Agra Fort", "type": "history", "entry": 650, "duration": "2 hours", "time": "Morning", "description": "Explore the fort complex and its views toward the Taj."},
        {"name": "Mehtab Bagh", "type": "nature", "entry": 200, "duration": "1 hour", "time": "Sunset", "description": "A garden viewpoint across the river; check access and sunset timing."},
        {"name": "Itimad-ud-Daulah's Tomb", "type": "history", "entry": 300, "duration": "1 hour", "time": "Afternoon", "description": "A smaller tomb complex with detailed stone inlay work."},
        {"name": "Sadar Bazaar", "type": "shopping", "entry": 0, "duration": "1–2 hours", "time": "Evening", "description": "Browse local goods and leave time to compare prices."},
        {"name": "Agra sweets tasting", "type": "food", "entry": 250, "duration": "1 hour", "time": "Evening", "description": "Try petha and other local sweets from an established shop."},
    ],
    "udaipur": [
        {"name": "City Palace", "type": "history", "entry": 400, "duration": "2–3 hours", "time": "Morning", "description": "Allow time for the courtyards, galleries, and lake views."},
        {"name": "Lake Pichola boat ride", "type": "nature", "entry": 500, "duration": "1 hour", "time": "Sunset", "description": "Check boat schedules and weather before joining the queue."},
        {"name": "Jagdish Temple", "type": "culture", "entry": 0, "duration": "45 minutes", "time": "Morning", "description": "A central temple visit; dress respectfully and check local guidance."},
        {"name": "Bagore Ki Haveli", "type": "culture", "entry": 150, "duration": "1–2 hours", "time": "Afternoon", "description": "Explore the historic haveli and check whether an evening show is running."},
        {"name": "Hathi Pol market", "type": "shopping", "entry": 0, "duration": "1–2 hours", "time": "Afternoon", "description": "Browse local art, textiles, and souvenirs at your own pace."},
        {"name": "Rajasthani thali", "type": "food", "entry": 500, "duration": "1 hour", "time": "Evening", "description": "Set aside time for a relaxed regional meal."},
    ],
    "jodhpur": [
        {"name": "Mehrangarh Fort", "type": "history", "entry": 400, "duration": "2–3 hours", "time": "Morning", "description": "Give yourself time for the museum and wide views over the blue city."},
        {"name": "Jaswant Thada", "type": "history", "entry": 50, "duration": "1 hour", "time": "Morning", "description": "A quiet marble memorial near the fort."},
        {"name": "Toorji Ka Jhalra", "type": "culture", "entry": 0, "duration": "45 minutes", "time": "Afternoon", "description": "A restored stepwell tucked into the old city lanes."},
        {"name": "Clock Tower and Sardar Market", "type": "shopping", "entry": 0, "duration": "1–2 hours", "time": "Afternoon", "description": "Explore the market streets and compare local crafts."},
        {"name": "Blue City walk", "type": "culture", "entry": 0, "duration": "1–2 hours", "time": "Evening", "description": "Take a respectful walk through the old lanes, ideally with a local guide."},
        {"name": "Marwari meal", "type": "food", "entry": 450, "duration": "1 hour", "time": "Evening", "description": "Try regional dishes at a local restaurant."},
    ],
    "varanasi": [
        {"name": "Dashashwamedh Ghat", "type": "culture", "entry": 0, "duration": "1 hour", "time": "Evening", "description": "Check local arrangements for the evening ceremony and arrive early."},
        {"name": "Sunrise boat ride", "type": "nature", "entry": 500, "duration": "1 hour", "time": "Morning", "description": "Agree the route and price before boarding; conditions can vary."},
        {"name": "Kashi Vishwanath area", "type": "culture", "entry": 0, "duration": "1–2 hours", "time": "Morning", "description": "Follow current entry, security, and photography guidance."},
        {"name": "Sarnath", "type": "history", "entry": 300, "duration": "2–3 hours", "time": "Afternoon", "description": "A nearby Buddhist heritage site; check museum opening hours."},
        {"name": "Old city lanes", "type": "culture", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "Explore slowly and be mindful around worshippers and residents."},
        {"name": "Banarasi food walk", "type": "food", "entry": 350, "duration": "1–2 hours", "time": "Evening", "description": "Sample local snacks and sweets from busy vendors."},
    ],
    "amritsar": [
        {"name": "Golden Temple", "type": "culture", "entry": 0, "duration": "2 hours", "time": "Morning", "description": "Cover your head, follow visitor guidance, and allow time to pause."},
        {"name": "Jallianwala Bagh", "type": "history", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "A solemn memorial visit; take time to read the displays."},
        {"name": "Partition Museum", "type": "history", "entry": 250, "duration": "1–2 hours", "time": "Afternoon", "description": "A thoughtful museum visit; verify opening days before going."},
        {"name": "Wagah-Attari border ceremony", "type": "culture", "entry": 0, "duration": "3 hours", "time": "Afternoon", "description": "Plan transport and arrive early; access rules may change."},
        {"name": "Hall Bazaar", "type": "shopping", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "Browse textiles, crafts, and everyday market stalls."},
        {"name": "Amritsari kulcha meal", "type": "food", "entry": 300, "duration": "1 hour", "time": "Evening", "description": "Make room for the city's well-known stuffed kulcha."},
    ],
    "kochi": [
        {"name": "Fort Kochi waterfront", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "Walk the waterfront and look for the Chinese fishing nets."},
        {"name": "Mattancherry Palace", "type": "history", "entry": 20, "duration": "1 hour", "time": "Morning", "description": "Check opening times before visiting this historic palace museum."},
        {"name": "Jew Town and Paradesi Synagogue area", "type": "culture", "entry": 0, "duration": "1–2 hours", "time": "Afternoon", "description": "Explore heritage lanes respectfully and verify site opening times."},
        {"name": "Kerala crafts and spice shops", "type": "shopping", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "Browse local stores and compare quality and prices."},
        {"name": "Kathakali performance", "type": "culture", "entry": 500, "duration": "1–2 hours", "time": "Evening", "description": "Check performance schedules and arrive early for context."},
        {"name": "Kerala seafood meal", "type": "food", "entry": 600, "duration": "1 hour", "time": "Evening", "description": "Try a regional meal; ask about spice levels and allergens."},
    ],
    "bengaluru": [
        {"name": "Lalbagh Botanical Garden", "type": "nature", "entry": 50, "duration": "1–2 hours", "time": "Morning", "description": "A relaxed garden walk; check special event access if visiting during a flower show."},
        {"name": "Bengaluru Palace", "type": "history", "entry": 300, "duration": "1–2 hours", "time": "Morning", "description": "Check current visitor rules and photography restrictions."},
        {"name": "Cubbon Park", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "A leafy break in the city center."},
        {"name": "National Gallery of Modern Art", "type": "culture", "entry": 20, "duration": "1–2 hours", "time": "Afternoon", "description": "Pick an exhibition that interests you and leave room to linger."},
        {"name": "Commercial Street", "type": "shopping", "entry": 0, "duration": "1–2 hours", "time": "Afternoon", "description": "Browse clothing, accessories, and local shops."},
        {"name": "South Indian breakfast", "type": "food", "entry": 250, "duration": "1 hour", "time": "Evening", "description": "Try dosa, idli, or another local favorite at a busy restaurant."},
    ],
    "kolkata": [
        {"name": "Victoria Memorial", "type": "history", "entry": 100, "duration": "2 hours", "time": "Morning", "description": "Explore the grounds and museum; check the current gallery schedule."},
        {"name": "Indian Museum", "type": "culture", "entry": 75, "duration": "2 hours", "time": "Morning", "description": "Choose a few collections rather than trying to see every gallery."},
        {"name": "Prinsep Ghat", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Sunset", "description": "A riverside walk that works well toward the end of the day."},
        {"name": "Kumartuli", "type": "culture", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "See traditional artisan workshops respectfully and ask before photographing."},
        {"name": "New Market", "type": "shopping", "entry": 0, "duration": "1–2 hours", "time": "Afternoon", "description": "A busy market for browsing; keep an eye on belongings."},
        {"name": "Bengali sweets tasting", "type": "food", "entry": 300, "duration": "1 hour", "time": "Evening", "description": "Try a few classic sweets from a well-established shop."},
    ],
    "chennai": [
        {"name": "Kapaleeshwarar Temple", "type": "culture", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "Check visitor guidance and dress respectfully."},
        {"name": "Government Museum", "type": "culture", "entry": 50, "duration": "2 hours", "time": "Morning", "description": "Pick a few galleries, including the collections you care about most."},
        {"name": "Marina Beach", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Sunset", "description": "Enjoy the shoreline from permitted areas and follow local safety guidance."},
        {"name": "Fort St. George", "type": "history", "entry": 25, "duration": "1–2 hours", "time": "Afternoon", "description": "Check museum opening times and access rules before setting out."},
        {"name": "T. Nagar shopping streets", "type": "shopping", "entry": 0, "duration": "1–2 hours", "time": "Afternoon", "description": "Browse textiles and local shops; traffic can make travel slow."},
        {"name": "Tamil meals tasting", "type": "food", "entry": 300, "duration": "1 hour", "time": "Evening", "description": "Try a local meals set and ask about spice levels if needed."},
    ],
    "hyderabad": [
        {"name": "Charminar", "type": "history", "entry": 25, "duration": "1 hour", "time": "Morning", "description": "Explore the landmark and surrounding old-city lanes."},
        {"name": "Chowmahalla Palace", "type": "history", "entry": 150, "duration": "1–2 hours", "time": "Morning", "description": "Allow time for the palace courtyards and exhibits."},
        {"name": "Salar Jung Museum", "type": "culture", "entry": 50, "duration": "2–3 hours", "time": "Afternoon", "description": "Choose a few collections in advance; the museum is extensive."},
        {"name": "Hussain Sagar promenade", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Sunset", "description": "A lakeside pause; check boat operations if you want to go out on the water."},
        {"name": "Laad Bazaar", "type": "shopping", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "Browse bangles and traditional goods around the old city."},
        {"name": "Hyderabadi biryani meal", "type": "food", "entry": 400, "duration": "1 hour", "time": "Evening", "description": "Choose a busy local restaurant and allow time for the meal."},
    ],
    "lucknow": [
        {"name": "Bara Imambara", "type": "history", "entry": 100, "duration": "2 hours", "time": "Morning", "description": "Explore the complex and follow guidance around the maze-like Bhul Bhulaiya."},
        {"name": "Chota Imambara", "type": "history", "entry": 100, "duration": "1 hour", "time": "Morning", "description": "A richly decorated historic complex; check current visitor rules."},
        {"name": "Residency ruins", "type": "history", "entry": 25, "duration": "1–2 hours", "time": "Afternoon", "description": "Walk the grounds and read the interpretive displays."},
        {"name": "Hazratganj", "type": "shopping", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "Browse the central shopping district and nearby cafes."},
        {"name": "Ambedkar Memorial Park", "type": "nature", "entry": 20, "duration": "1 hour", "time": "Evening", "description": "A spacious outdoor complex; check access hours before visiting."},
        {"name": "Awadhi food stop", "type": "food", "entry": 500, "duration": "1–2 hours", "time": "Evening", "description": "Try regional kebabs or a slow-cooked Awadhi dish."},
    ],
    "mysuru": [
        {"name": "Mysore Palace", "type": "history", "entry": 100, "duration": "2 hours", "time": "Morning", "description": "Check the palace's current visiting and photography rules."},
        {"name": "Chamundi Hill", "type": "culture", "entry": 0, "duration": "1–2 hours", "time": "Morning", "description": "Plan transport and be mindful around the temple and visitors."},
        {"name": "St. Philomena's Church", "type": "history", "entry": 0, "duration": "45 minutes", "time": "Afternoon", "description": "A short architectural stop; avoid disrupting services."},
        {"name": "Brindavan Gardens", "type": "nature", "entry": 50, "duration": "2 hours", "time": "Evening", "description": "Check fountain-show timings and transport before heading out."},
        {"name": "Devaraja Market", "type": "shopping", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "Browse flowers, produce, and local goods with a camera-ready eye."},
        {"name": "Mysore cuisine stop", "type": "food", "entry": 300, "duration": "1 hour", "time": "Evening", "description": "Make time for a local meal or Mysore pak from a trusted shop."},
    ],
    "shimla": [
        {"name": "The Ridge", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "A central open space for mountain views and a gentle walk."},
        {"name": "Christ Church", "type": "history", "entry": 0, "duration": "45 minutes", "time": "Morning", "description": "Visit respectfully and check whether services are underway."},
        {"name": "Viceregal Lodge", "type": "history", "entry": 100, "duration": "1–2 hours", "time": "Afternoon", "description": "Check guided-tour availability and current opening hours."},
        {"name": "Mall Road", "type": "shopping", "entry": 0, "duration": "1–2 hours", "time": "Evening", "description": "Walk the pedestrian stretch and browse at a relaxed pace."},
        {"name": "Jakhoo area", "type": "nature", "entry": 0, "duration": "1–2 hours", "time": "Morning", "description": "Plan the uphill journey and follow local guidance around wildlife."},
        {"name": "Himachali meal", "type": "food", "entry": 450, "duration": "1 hour", "time": "Evening", "description": "Try a regional meal at a local restaurant."},
    ],
    "manali": [
        {"name": "Hadimba Devi Temple", "type": "culture", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "Visit respectfully and allow time to walk through the surrounding cedar forest."},
        {"name": "Old Manali walk", "type": "culture", "entry": 0, "duration": "1–2 hours", "time": "Morning", "description": "Explore cafes and lanes without rushing between stops."},
        {"name": "Manu Temple area", "type": "history", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "Check access and local conditions before making the uphill walk."},
        {"name": "Vashisht hot springs area", "type": "culture", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "Follow local bathing rules and check current access."},
        {"name": "Solang Valley outing", "type": "nature", "entry": 500, "duration": "3 hours", "time": "Morning", "description": "Weather and activity prices vary; confirm conditions and operators locally."},
        {"name": "Himachali cafe meal", "type": "food", "entry": 400, "duration": "1 hour", "time": "Evening", "description": "Leave time for a warm meal after exploring outdoors."},
    ],
    "rishikesh": [
        {"name": "Triveni Ghat", "type": "culture", "entry": 0, "duration": "1 hour", "time": "Evening", "description": "Check the local ceremony schedule and respect the riverside customs."},
        {"name": "Ram Jhula", "type": "history", "entry": 0, "duration": "45 minutes", "time": "Morning", "description": "Walk across when open and be mindful of local traffic and pedestrians."},
        {"name": "Beatles Ashram", "type": "culture", "entry": 200, "duration": "1–2 hours", "time": "Afternoon", "description": "Check entry conditions and allow time for the forested paths and artwork."},
        {"name": "Ganga riverside walk", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "Keep to safe public paths and follow river-safety notices."},
        {"name": "Local yoga class", "type": "culture", "entry": 500, "duration": "1 hour", "time": "Morning", "description": "Book directly with a reputable studio and check the class level."},
        {"name": "Pahadi cafe meal", "type": "food", "entry": 350, "duration": "1 hour", "time": "Evening", "description": "Try a relaxed local meal after a day by the river."},
    ],
    "srinagar": [
        {"name": "Dal Lake shikara ride", "type": "nature", "entry": 800, "duration": "1–2 hours", "time": "Morning", "description": "Agree on duration, route, and total price before boarding."},
        {"name": "Mughal Gardens", "type": "nature", "entry": 50, "duration": "1–2 hours", "time": "Morning", "description": "Choose a garden based on the season and check current opening times."},
        {"name": "Shankaracharya Temple area", "type": "culture", "entry": 0, "duration": "1–2 hours", "time": "Afternoon", "description": "Check security and access guidance before travelling up the hill."},
        {"name": "Old Srinagar heritage walk", "type": "history", "entry": 0, "duration": "1–2 hours", "time": "Afternoon", "description": "Consider a local guide to understand the architecture and neighborhood history."},
        {"name": "Local handicraft shops", "type": "shopping", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "Compare materials and prices, especially for higher-value crafts."},
        {"name": "Kashmiri meal", "type": "food", "entry": 600, "duration": "1 hour", "time": "Evening", "description": "Try a regional dish and ask about spice level and ingredients."},
    ],
    "darjeeling": [
        {"name": "Tiger Hill sunrise", "type": "nature", "entry": 0, "duration": "2 hours", "time": "Morning", "description": "Start early and remember that mountain views depend on weather."},
        {"name": "Batasia Loop", "type": "history", "entry": 50, "duration": "1 hour", "time": "Morning", "description": "A railway landmark with a garden and mountain views on clear days."},
        {"name": "Himalayan Mountaineering Institute", "type": "culture", "entry": 100, "duration": "1–2 hours", "time": "Afternoon", "description": "Check museum and zoo schedules before combining visits."},
        {"name": "Darjeeling Himalayan Railway ride", "type": "history", "entry": 1000, "duration": "2 hours", "time": "Afternoon", "description": "Book and verify the route and fare with the official railway source."},
        {"name": "Chowrasta and Mall Road", "type": "shopping", "entry": 0, "duration": "1 hour", "time": "Evening", "description": "Browse small shops and take a relaxed walk around the square."},
        {"name": "Tea tasting", "type": "food", "entry": 350, "duration": "1 hour", "time": "Evening", "description": "Try local tea and check whether the estate or shop offers tastings."},
    ],
    "pune": [
        {"name": "Shaniwar Wada", "type": "history", "entry": 25, "duration": "1 hour", "time": "Morning", "description": "Explore the historic fortification and its grounds."},
        {"name": "Aga Khan Palace", "type": "history", "entry": 25, "duration": "1–2 hours", "time": "Morning", "description": "A significant historical site; allow time for the exhibits and grounds."},
        {"name": "Raja Dinkar Kelkar Museum", "type": "culture", "entry": 100, "duration": "1–2 hours", "time": "Afternoon", "description": "A collection-rich museum; select a few areas to focus on."},
        {"name": "Vetal Tekdi", "type": "nature", "entry": 0, "duration": "1 hour", "time": "Morning", "description": "A nature walk; use marked paths and avoid hot parts of the day."},
        {"name": "FC Road", "type": "shopping", "entry": 0, "duration": "1 hour", "time": "Afternoon", "description": "Browse the lively student-area shops and cafes."},
        {"name": "Maharashtrian meal", "type": "food", "entry": 350, "duration": "1 hour", "time": "Evening", "description": "Try a local thali or regional snack."},
    ],
}

# Common alternate spellings and broad destination labels.
DESTINATION_ALIASES = {
    "new delhi": "delhi", "ncr": "delhi", "bombay": "mumbai", "panaji": "goa",
    "cochin": "kochi", "mysore": "mysuru", "banaras": "varanasi", "benaras": "varanasi",
    "kashi": "varanasi", "simla": "shimla", "rishikesh uttarakhand": "rishikesh",
}
ALIASES = {
    "heritage": "history", "historic": "history", "museum": "culture", "museums": "culture",
    "beach": "nature", "beaches": "nature", "outdoors": "nature", "outdoor": "nature",
    "local cuisine": "food", "cuisine": "food", "restaurants": "food", "market": "shopping",
    "markets": "shopping", "shopping and markets": "shopping", "arts": "culture",
}


def _normalise_destination(destination: str | None) -> str:
    key = " ".join((destination or "Jaipur").strip().lower().replace(", india", "").split())
    key = DESTINATION_ALIASES.get(key, key)
    return key


def list_destinations():
    """Return supported destination labels for the website dropdown."""
    return [{"value": key, "label": key.title()} for key in sorted(DESTINATIONS)]


def _places(destination):
    """Return sample places for a supported destination, or an empty list."""
    key = _normalise_destination(destination)
    return DESTINATIONS.get(key, [])


def find_places(destination="Jaipur", interests=None, limit=8):
    """Find sample attractions for a destination and interests."""
    key = _normalise_destination(destination)
    places = list(_places(destination))
    normalised_interests = [ALIASES.get(str(i).strip().lower(), str(i).strip().lower()) for i in (interests or [])]
    if normalised_interests:
        preferred = [p for p in places if p["type"] in normalised_interests]
        places = preferred + [p for p in places if p not in preferred]
    return {
        "destination": (destination or "Jaipur").strip().title(),
        "results": places[:max(1, min(int(limit), 12))],
        "source": "sample demo dataset",
        "supported": bool(DESTINATIONS.get(key)),
    }


def estimate_trip_budget(destination="Jaipur", days=3, travelers=2, budget_inr=12000, travel_style="balanced"):
    """Estimate trip costs in INR. This is not a live quote."""
    days = max(1, min(int(days), 7))
    travelers = max(1, min(int(travelers), 12))
    budget_inr = max(0, int(budget_inr))
    stay_per_night = {"budget": 900, "balanced": 1800, "comfort": 3500}.get(travel_style, 1800)
    transport_per_person_day = {"budget": 250, "balanced": 450, "comfort": 900}.get(travel_style, 450)
    stay = stay_per_night * travelers * max(0, days - 1)
    food = 650 * travelers * days
    transport = transport_per_person_day * travelers * days
    activities = 500 * travelers * days
    total = stay + food + transport + activities
    return {
        "currency": "INR", "budget_inr": budget_inr,
        "estimated": {"stay": stay, "food": food, "local_transport": transport, "activities": activities, "total": total},
        "remaining": budget_inr - total, "within_budget": total <= budget_inr,
        "assumptions": ["Illustrative estimates only, not live prices.", "Stay estimate uses days minus one nights.", "Intercity transport is not included."],
    }


def create_itinerary(destination="Jaipur", days=3, travelers=2, budget_inr=12000, interests=None, travel_style="balanced"):
    """Build a day-by-day sample itinerary and budget estimate."""
    days = max(1, min(int(days), 7))
    travelers = max(1, min(int(travelers), 12))
    found = find_places(destination, interests, limit=12)
    results = found["results"]
    itinerary = []
    slots = ["Morning", "Afternoon", "Evening"]
    for day in range(days):
        activities = []
        for slot in range(3):
            idx = day * 3 + slot
            if idx < len(results):
                place = results[idx]
                activities.append({
                    "time": slots[slot], "name": place["name"], "duration": place["duration"],
                    "entry_cost_per_person": place["entry"], "type": place["type"],
                    "description": place.get("description", "A suggested stop for your trip."),
                })
        itinerary.append({"day": day + 1, "title": f"Day {day + 1}", "activities": activities})

    notes = [
        "Opening hours, entry fees and availability can change; check official sources before you go.",
        "Travel time between stops is not modelled, so leave buffer time for traffic and breaks.",
        "No booking is made. These are planning estimates, not live prices or quotes.",
    ]
    if not found["supported"]:
        notes.insert(0, f"We don't have a curated sample attraction list for {destination!s} yet. Add it to DESTINATIONS in travel_tools.py; no other city's attractions have been substituted.")
    elif len(results) < days * 3:
        notes.insert(0, f"This sample dataset has {len(results)} suggested stops, so some days may have fewer than three activities.")

    return {
        "destination": (destination or "Jaipur").strip().title(), "days": days, "travelers": travelers,
        "travel_style": travel_style, "interests": interests or [], "itinerary": itinerary,
        "budget": estimate_trip_budget(destination, days, travelers, budget_inr, travel_style), "notes": notes,
        "destination_supported": found["supported"],
    }


def replan_trip(destination="Jaipur", days=3, travelers=2, budget_inr=12000, interests=None, travel_style="budget"):
    """Rebuild the plan after preferences or budget change."""
    plan = create_itinerary(destination, days, travelers, budget_inr, interests, travel_style)
    plan["replanned"] = True
    plan["replan_reason"] = "Updated using the latest budget, travel style and interests."
    return plan
