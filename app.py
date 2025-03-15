from flask import Flask, jsonify
import random

app = Flask(__name__)

forts = [
    {
"name": "Lohagadh Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/shutterstock_707946589lohagard.jpg",
"about": "Among the many hill forts in Maharashtra, Lohagadh is a marvelous piece of architecture. Located 52 km northwest of Pune, the fort sits at an elevation of 1,033 m above sea level. In 1648 CE, the fort was captured by Shivaji, which was then captured by the Mughals in 1665 CE. In 1670 CE, Shivaji Maharaj captured the fort again and he used it to store his treasury looted from Surat. Lohagadh fort is also one of the scenic treks in Pune that can be done in a day."
},
{
"name": "Murud-Janjira Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/murud-fort-kb6592.jpg",
"about": "Janjira fort, which is popular as Murud Fort, is located in Murud village of Maharashtra. Among the most impressive forts near Pune, Janjira is surrounded by water on all sides. Built by Malik Ambar at the end of the 17th century, the fort reflects the marvel of ancient engineering. This brilliant fort stands at a height of 40 feet, enduring the lashes of sea waves for ages. The fort had 500 canons but only a few of them are left now, and its towers are now used to keep guns in them."
},
{
"name": "Daulatabad Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/daulatabad-for-kb6592.jpg",
"about": "Daulatabad Fort, which is also known as Devagiri was built in the 14th century. Situated at a distance of 16 km northwest of Aurangabad, this fort is considered one of the seven wonders of Maharashtra. Among the most gorgeous forts in Maharashtra, Daulatabad was captured by various rulers, including the Mughals, the Marathas, and the Peshwas. In 1724 AD, it came under the Nizams of Hyderabad. In order to reach the fort, you have to climb about 750 steps, which makes it a great hike."
},
{
"name": "Panhala Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/panhala-fort-kb6592.jpg",
"about": "20 km away from the main city of Kolhapur, Panhala Fort is strategically situated looking over a pass, which was a major trade route from Bijapur in the interior of Maharashtra, in the majestic Sahyadri mountain range. Tarabai, the queen regent of Kolhapur spent her formative years in the fort. Some parts of the fort are still intact making it a must-visit destination in Maharashtra."
},
{
"name": "Raigadh Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/1200px-Raigad_fort_towers.jpg",
"about": "Located at a height of 820 m, Raigadh Fort is perched on the lush green Sahyadri mountain range. Climbing 1737 steps will take you to the fort, which offers spectacular views of the valley down below. One of the most popular forts in Maharashtra, it was considered the most secure fort in the entire region. Great pride of the Marathas, the fort tells the story of their glorious past."
},
{
"name": "Shanivarwada Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/shutterstock_715593082shanivar-vada-fort1.jpg",
"about": "Shanivarwada fort was the seat of the Maratha empire between 1730 to 1818. Among the most stunning forts in Pune, this one holds a special and an important place in Indian history. Built by the Peshwas of Chhatrapati, this palace fort has nearly been destroyed by military attacks and was majorly by an unexplained fire in 1828. It is also believed that the fort palace is haunted by the ghost of Peshwa Narayanro."
},
{
"name": "Yashwantgarh Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/shutterstock_722994715Yashwantgad-Fort1.jpg",
"about": "Situated near Maharashtra-Goa border, Yashwantgadh fort mainly ruins now. Also known as Redi fort, it was built by the Marathas in the 16th century. The fort was captured by the British in 1765, who later sold the land to locals in 1890 retaining the ownership of the fort walls. If you're someone who considers ruins beautiful, you must pay a visit to the fort."
},
{
"name": "Sindhugarh Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/sindhugarh-fort-kb6592.jpg",
"about": "Sindhugarh fort was erected by Shivaji Maharaj in 1664-67 AD on 48 acres of the island. It is believed that he personally selected this location, which is a rocky island. The most amazing feature of the fort is that its foundation stones were laid down firmly in molten lead. The solid walls and beautiful gateways of this fort make it look absolutely majestic."
},
{
"name": "Sinhagadh Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/Sinhagad-Fort-kb6592.jpg",
"about": "Sinhagadh fort is situated on a hill located about 25 km southwest of Pune. It is located at an elevation of 1,312 m above sea level. Some of the sources say that the fort could have been built over 2000 years ago. The fort was formerly known as Kondhana, which has witnessed many battles through the centuries, and the most important one was the Battle of Sinhagad in 1670."
},
{
"name": "Pratapgad Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/Pratapgad-Fort-kb6592.jpg",
"about": "A Shivaji Maharaj fort, Pratapgad is a huge fort located in Satara. As per the records, the fort was built in 1657, offering a mesmerizing view of coastal Konkan. At a distance of only 8 km from Mahabaleshwar, this is among the most popular forts in Maharashtra. In 1960, a guest house and a national park were established inside the fort."
},
{
"name": "Torna Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/FotoJet6592thfyg1.jpg",
"about": "One of the must-visit forts in Pune, Torna Fort is also known as Prachandagad. It is situated at an elevation of 1,403 m above sea level, which makes it the highest hill fort in Pune. It is historically an important monument as it was the first fort captured by Shivaji Maharaj in 1643 when he was 16. With gorgeous towers and monuments built inside the fort, it certainly is a piece of architectural wonder."
},
{
"name": "Kandhar Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/Indien2012_1253_Kandhar_Fort.jpg",
"about": "Located at a distance of 50 km from Ranthambhore National Park, Kandhar Fort was built nearly 1200 years ago by King Krishna III of Malkhed. Its architecture is quite similar to that of the Shivneri forts in Maharashtra. Known for its wonderful architecture, it is surrounded by a canal filled with water."
},
{
"name": "Rajmachi Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/Rajmachi-Fort.jpg",
"about": "One of the most beautiful forts in Maharashtra, the Rajmachi Fort is formed when two forts namely Manaranjan Fort and Shrivardhan Fort come together. Located in a village known as Rajmachi in the mountains of Sahyadri, this fort is pretty famous and a must-visit place in Maharashtra. You will find nature at its best here."
},
{
"name": "Tikona Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/Tikona-Fort.jpg",
"about": "Tikona when translated means ‘triangle. 3500 feet high and pyramidal in shape Tikona Fort is located near Lonavala and offers impeccable views. Probably the most instagrammable fort in Maharashtra this fort is also a famous trekking place and is popular for its large doors."
},
{
"name": "Vasota Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/Vasota-Fort.jpg",
"about": "Offering awe-inspiring views of Shivsagar lake and Nageshwar peak, Vasota Fort is created by the backwaters of Koyna river and is gorgeous. What is more beautiful is the road leading to the fort. Passing through Kas pathar or as it is popularly known as the Valley of Flowers of Maharashtra, you will encounter spectacular views along the way."
},
{
"name": "Visapur Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/Visapur-Fort.jpg",
"about": "Also known as the Visapoor Fort, this fort in Maharashtra is a part of the Visapur-Lohagarh fortification which happened back in the day. Situated near the village Visapur this fort is extremely beautiful and is located at a height of 1084 meters. It's quite high above sea level and its beauty will leave you spellbound."
},
{
"name": "Suvarnadurg Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/Suvarnadurg-Fort.jpg",
"about": "Imagine visiting a sea fort. Now read about Suvarnadurg Fort and tell us if there is any reason as to why you shouldn’t visit this beautiful sea fort in Maharashtra. Situated on a small island within the Arabian Sea and close to Harnai this fort is as beautiful as it gets. Established by Marathas this fort is nothing less than magical."
},
{
"name": "Korigad Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2018/01/Korigad-Fort.jpg",
"about": "Also known as Koraigad, the Korigad Fort is hardly at a 20-kilometer distance from Lonavala and near a village called Peth Shahpur. Made during the reign of Chatrapati Shivaji the Tung Fort is an important historical site that you must not miss out on when in Maharashtra. If you are a history lover you will instantly fall in love with this place. The view from this Maharastra fort is truly amazing."
},
{
"name": "Akola Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/13.jpg",
"about": "Also known as the Asadgad fort, this classic structure is one of the most significant fortifications of the Akola district. If you are planning a cultural tour in Maharashtra, chances are that this place is going to be one of the top sightseeing attractions on your list. The initial construction of the fort was done using mud by Akol Singh and later was turned into a solid architectural marvel that we all observe today."
},
{
"name": "Vasai Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/21.jpg",
"about": "Popularly known among the locals as Corte de Baçaim meaning \"Court of Bassein\" or Fort Bassein, this popular ruins area is a major attraction among tourists for its association with the historical chapter of Palghar district of Konkan. If you are in the state for a few days and looking for an enthralling historical journey, this is the place to be."
},
{
"name": "Prabalgad Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/2-1.jpg",
"about": "Located at the intersection of Matheran and Panvel, the Prabalgad Fort is a timeless piece of architecture that stands tall amidst barren lands of history. Nestled in front of the mountain ranges of Sahyadris, it is a popular sightseeing location for tourists and a weekend getaway place for those locals and state natives."
},
{
"name": "Harishchandragad Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/2-2.jpg",
"about": "More than just a hill fort in Ahmednagar, this is not just another sightseeing attraction, but a landmark that literally controls the surrounding regions. The best way to explore this place is by taking a hike to the top, taking detours to viewpoints, and enjoying an afternoon camping in the surrounding spaces."
},
{
"name": "Mandangad Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/2-3.jpg",
"about": "Located at a distance of 2 km from Mandangad town, this fort has majestic views, classic architecture, and a 400-year-old cannon that is the main attraction of this site. Come for the historical tour and stay for the views, enjoy a little picnic by its side, and don't forget to snap some photographs of this marvel before you leave."
},
{
"name": "Vijaydurg Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/2-4.jpg",
"about": "This epic gem of Maharashtra is a rare attraction that is surrounded by the sea on all four sides. The Vijaydurg Fort is the oldest fort and archeological structure that is located on the Sindhudurg coast. Constructed during the rule of Raja Bhoj, today it is a popular sight for tourists to enjoy sightseeing."
},
{
"name": "Shaniwarwada Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/2-5.jpg",
"about": "This 18th-century historical fort built-in 1732 is a popular sight that documents many events of the Maratha Empire and traces their time in this region. It is advised that during your tour of the fort, make sure you have a local or tour guide who can help in breaking down the story and time periods that are of importance to this site."
},
{
"name": "Ghangad Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/2-6.jpg",
"about": "Located at a distance of 30 kilometers from Lonavla-Khandala and 100 kilometers from Pune, this 300-years-old fort is a prime part of most history tours in the district. Currently, this structure is being under restoration by the Shivaji Trail group in association with the local people."
},
{
"name": "Purandar Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/2-7.jpg",
"about": "This historical mountaintop fort is one of the best viewpoints in Maharashtra that offers you a panoramic view of the surrounding regions. Situated at a height of 4472 ft above sea level, the fort is very much of significance in the locale for its symbolism of Shivaji against Adil Shahi Bijapur Sultanate."
},
{
"name": "Malhargad Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/2-8.jpg",
"about": "If you are taking a trip to or around Pune, this fort is one of the most popular 18th-century architectures this is definitely worth a detour. It is also a great place to visit for a short-day trekking experience with your family and friends. Also known as Sonuricha Killa, a 30-minute hike to the top will give you majestic views of the surrounding area."
},
{
"name": "Tung Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/2-9.jpg",
"about": "Tung Fort is one of Maharashtra's classic hill forts popularly visited by tourists for trekking and sightseeing activities. It stays extraordinary compared to other fortifications in the state. Based on higher ground, it is the most panoramic view point with all-encompassing perspectives across Maharashtra."
},
{
"name": "Shivneri Fort",
"image": "https://assets.traveltriangle.com/blog/wp-content/uploads/2019/01/2-10.jpg",
"about": "Nestled in the northern region of the Pune district, Shivneri Fort is one of the most classic attractions that hold cultural significance, largely due to the fact that the marvelous structure is the birthplace of Chhatrapati Shivaji Maharaj."
}
]

@app.route("/")
def get_fort():
    fort = random.choice(forts)
    return jsonify(fort)

if __name__ == "__main__":
    app.run(debug=True,port=8081)
