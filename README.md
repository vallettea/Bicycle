Bicycle
=======

I have so much pleasure riding my own handmade bicycle that I want to share the way I did it.

### Design a bike that fits your body

Framebuilding isn't knew and some books are explaining the process. Among them, the [patereck](http://www.amazon.com/The-Paterek-manual-bicycle-framebuilders/dp/B000711OC0) which can be find free of charge [here](http://www.timpaterek.com/paterek.pdf), is the one I used. 

![Exerpt from the Patereck](img/patereck.png "Exerpt from the Patereck")

It explains all the rules needed to match the size of your frame to the size of your body. 
To facilitate the process, I have written all the measures you need inside a little python script called `patereck.py` available in this repo:

```python
#### parameters to choose:
##### rider
A = 82 # inseam height
cubit = 46 # from elbow to nails, hand opened
TM = 67 # torso measurment
AM = 66 # arm measurment

##### bike
B = 27 # bottom braket height in cm
C = 4 # crotch clearance (4cm for touting 6cm for racing)
E = radians(73.2) # seat tube angle
HTA = radians(72) # head tube angle:70:resilient and confort (touring) 75: stiff (race)
FR = 4.5 # fork rake: + for touring - for race
R = 33.4 # wheel radius
```

once you run it using `python patereck.py` you'll find all the measurements you need:

```
Down Tube : 51
Seat Tube : 53.273750437
Top Tube : 54.3
========== checks ===========
Stem from torso: 3.52608695652
Stem form cubit: 9.2
Trail (5 to 7):  6.12073784511
Front center (around 58)
chainstay (40 for race to 47 for touring
check clearance
```

there are two ways to compute the stem and I guess I misunderstood one because both don't give me the same result. I chose the one derived from the cubit.

Once you've got these measurments, download [RattleCad](http://rattlecad.sourceforge.net/) which is a free, open source version of BikeCad. It is far from being perfect but it does the work for the frame ajustments and mitering:

![frame](img/frame.png "Frame")
![completebike](img/completebike.png "Complete Bike")

The mitering is particularly usefull as if you take care of **printing these images without resizing**, you'll just have to cut them and round them on your tube to cut them properly.

![miter](img/miter.png "Mitering")


## Building

And now you're ready to do real stuff:

{% include image.html url="img/photo1.JPG" description="The trace you draw with the mitering paper." %}
{% include image.html url="img/photo2.JPG" description="Alignement is key here." %}
{% include image.html url="img/photo3.JPG" description="Use the eyelets to align the front dropouts." %}
{% include image.html url="img/photo16.JPG" description="My atelier." %}
{% include image.html url="img/photo4.JPG" description="After brazing the fork." %}
{% include image.html url="img/photo5.JPG" description="Don't forget to make holes where tubes will be brazed." %}
{% include image.html url="img/photo6.JPG" description="If the mitering is well adjusted then the tubes fit perfectly." %}
{% include image.html url="img/photo7.JPG" description="My marble is a thick glass." %}
{% include image.html url="img/photo8.JPG" description="I built a vernier with a sheet of metal where I've welded a caliper upside down." %}
{% include image.html url="img/photo9.JPG" description="Just point on the marble and weld afterwards." %}
{% include image.html url="img/photo10.JPG" description="For the rear dropouts, I've built a jig using a metal bar and two big screws." %}
{% include image.html url="img/photo11.JPG" description="A trick to adjust break bosses." %}
{% include image.html url="img/photo12.JPG" description="Front." %}
{% include image.html url="img/photo13.JPG" description="Rear. I've used a piece of copper because I had no more metal..." %}
{% include image.html url="img/photo14.JPG" description="Starting to look like a bike." %}
