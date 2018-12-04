from connection import coll
posts = [
	{
		"post_date": datetime.strptime("2018-03-01", "%Y-%m-%d"),
		"post_title": "The Day and Life of a Cat",
		"post_text": "Scratch at the door then walk away purrrrrr that box? i can fit in that box yet meow to be let in scratch at the door then walk away. Chase the pig around the house head nudges . Wack the mini furry mouse cats go for world domination chase dog then run away.",
		"post_tags":["if cats could talk", "cat latin"]
	},
	{
		"post_date": datetime.strptime("2018-03-10", "%Y-%m-%d"),
		"post_title": "Have ya ever been to sea Billy?",
		"post_text": "Bilged on her anchor knave scurvy rutters bilge water Corsair cable parley chase red ensign. Reef sails Shiver me timbers ye handsomely lugsail booty scallywag loot yard rigging. Spanish Main brig weigh anchor landlubber or just lubber Shiver me timbers deadlights spyglass yawl run a shot across the bow broadside.",
		"post_tags":["Pirates", "Captain Highliner", "Billy"]
	},
	{
		"post_date": datetime.strptime("2018-03-11", "%Y-%m-%d"),
		"post_title": "The Dawning of the Dead",
		"post_text":"Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis.",
		"post_tags":["Zombies", "Whitewalkers", "Dead"]
	},
	{
		"post_date":datetime.strptime("2018-03-11", "%Y-%m-%d"),
		"post_title": "Pig Latin",
		"post_text": "Spicy jalapeno bacon ipsum dolor amet voluptate nostrud pork belly sirloin t-bone sed non. In turducken fugiat leberkas nostrud cupim. Anim pork chop pork cupim minim tail id kevin ground round. Strip steak alcatra ex cow laboris short ribs quis. Boudin nisi labore, ullamco salami pork chop nulla quis deserunt meatloaf qui prosciutto beef. Beef kielbasa consectetur alcatra ullamco short loin commodo cillum sirloin.",
		"post_tags":["pork", "bacon", "meat"]	
	},
	{
		"post_date":datetime.strptime("2018-03-12", "%Y-%m-%d"),
		"post_title": "Monty Python's Flying Circus",
		"post_text": "And the hat. She's a witch! Ni! Ni! Ni! Ni! Ah, now we see the violence inherent in the system! On second thoughts, let's not go there. It is a silly place. Well, how'd you become king, then? You don't vote for kings.",
		"post_tags": ["Ni", "Witches", "Spot the loonie"]
	},
		{
		"post_date":datetime.strptime("2018-11-12", "%Y-%m-%d"),
		"post_title": "I videotape every customer that comes in here, so that I may blackmail them later",
		"post_text": "Bender, being God isn't easy. If you do too much, people get dependent on you, and if you do nothing, they lose hope. You have to use a light touch. Like a safecracker, or a pickpocket. Kids don't turn rotten just from watching TV",
		"post_tags": ["See-TV", "God Complex"]
	},
	{
		"post_date":datetime.strptime("2018-11-13", "%Y-%m-%d"),
		"post_title": "Bob Ross Speaks",
		"post_text": "Think about a cloud. Just float around and be there. Be careful. You can always add more - but you can't take it away. Decide where your cloud lives. Maybe he lives right in here. Almost everything is going to happen for you automatically - you don't have to spend any time working or worrying. Put light against light - you have nothing. Put dark against dark - you have nothing. It's the contrast of light and dark that each give the other one meaning",
		"post_tags": ["Clouds", "Beauty", "Artistic Balance"]
	},
    {
		"post_date":datetime.strptime("2018-11-15", "%Y-%m-%d"),
		"post_title": "Embracing my Inner Hipster",
		"post_text": "Lumbersexual celiac microdosing plus 1 salvia. Chartreuse brunch polaroid trust fund cloud bread. Lomo gluten-free bushwick vape asymmetrical wayfarers, iceland tumblr affogato pinterest. Lomo brooklyn gastropub chambray. Man buns and hipster lanyards",
		"post_tags": None
	}
]
result = coll.insert_many(posts)
num_posts = len(result.inserted_ids)
print("{} posts added to the blogs collection".format(num_posts))
