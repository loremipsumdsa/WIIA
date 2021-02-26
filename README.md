# What Is It About
## An automatic brainstorming to find correlation between concepts

We now that inteligence is making link between concepts, like if I say "burger" you think "food", that's how you think.
Now you also attribute a weight to that link, like I say "Burger", you think "food" but you also think "mcdonald", then there is a link between "food" and "mcdonald" but it is a bit less important than between "burger" and "food". 

So you know there is a link between burger and food because of your experience, if you want a burger you want food and if you want food you want a burger, that's the link. My computer dont want burger so it do not have any experience. It only have massive data.

The point with World Wild Web is that it is full of links, virtual links I mean, reference from a page to an other. What if we remplace link created with experience by those virtual link?

That what we are doing here : starting from a random word, found some words it is linked with and calculate how much it is linked with by exploring a kind of massive dictionnary : Wikipedia.org.
Of course for the computer there is still no sens, just a statistic proximity. but the result is pretty close with a brainstorming we could put on a blackboard (but bigger and faster).

A problem with that kind of analyse is that there are reccurent statistics errors : For exemple on a lot of wikipedia's pages, there is a reference to "ISBN" witch is a standard documents identifier, often in the citations section. It appear in the most of wikipedia's pages as it is out-of-subject. To avoid conclusion like "all is about ISBN", we can buid a blackist of concepts witch are always out of subject. It become interresting when that task is automatic: In fact it is pretty simple to find witch word are abnormally current by looking at a lot of pages randomly choosen. This is the purpose of the `learn` function.        




PS :

My name is Paul Nautré, i am a first Year student in a computer science's french University. I do not pretend to invent anything, just trying do lead some little projects to get experience. Also i'm new on GitHub and my english is may pretty bad, sorry about that
Thanks for your patience !  
