---
generator: pandoc
title: inglertChapterFour_210629
viewport: width=device-width, initial-scale=1.0, user-scalable=yes
---

Chapter Four: Jeu de Formes Assemblées dans la Lumière (Play of Forms in
Light)

Eric Todd Inglert, AIA

29 Jun 2021

## Monochromatic Tone Value Delineation

Grisaille is a painting technique that uses only one color, usually
gray, in a range of shades or values. It often serves as an
underpainting stage when using opaque paints. The most common way to
describe paint is by color. How do we reconcile these two seemingly
contradictory descriptions? Is it value or color? Yes!

\<Insert Figure 4.1.1\>

Figure 4.1.1: Medium Gray Reference Box

Figure 4.1.1 was drawn for illustration purposes here using a scalable
vector program called Inkscape. Let's describe it. It was originally
drawn to be 1 inch square (25mm). It has no outline color, and the fill
was selected as 50% gray. Let's dig a little deeper into our simple
square. Since Inkscape is a vector drawing program, then the code for
the file is text readable. It shows the following attribute:
fill:\#808080;stroke:none;stroke-width:0

For reference, fill is the color inside the square, stroke is the line
bounding the square and stroke-width is the thickness of that line. What
is \#808080? It turns out that this is a very specific color readable on
web pages. It is known as a *color hex value* and does not have much
value for our understanding. Let's dig a little deeper and translate
this description into terms more familiar to us. What are other ways of
describing color?

In kindergarten you no doubt learned of the primary colors: red, blue
and yellow. Later perhaps in high school physics you learned that the
primary colors in light are red, blue and green. In kindergarten we
mixed tempera paints of blue and red together to get purple...two
primary colors make a secondary color. Theoretically if we mix the three
primary colors in equal measure, then we should get a neutral gray like
the square above in the figure. In real life it is much closer to brown.
Incidentally, when mixing red light together with blue light you will
get a very different color, magenta. Magenta is not purple!

Since we are working in both the world of physical pigments and digital
light, we are going to need a more complex definition of color. This
will eventually lead us back to the idea of our 50% gray square in the
figure. Hex color \#808080 can also be defined in at least four
different ways: RGB, HSL, HSV and CYMK. Here is a table of these values
for 50% gray.

  ------ ------- ------- ------- -----
                                 
  RGB    128.0   128.0   128.0   
  HSL    0.0     0.0     0.5     
  HSV    0.0     0.0     50.0    
  CMYK   0.0     0.0     0.0     0.5
  ------ ------- ------- ------- -----

RGB stands for red, green and blue. These are known as channels. Each
channel has a range from 0 to 255. By inference we can say that light in
the amounts of half the range 128 of three channels when mixed is 50%
gray. If a web page presented the square in the figure above on a
computer monitor, then we could infer that it would consist of an area
of 72 ppi or pixels per inch. A pixel with a value of 128 would be
halfway between no light and all light. Could we use the metaphor of a
rheostat or dimmer on a light switch? A rheostat controls the amount of
current by varying the resistance. The more current that passes, then
the brighter the light. Leaving the metaphor behind, we can say that
while a computer bit has only two states, 0 or 1 (off or on,) our pixel
above has 256 discrete states. This is a pretty good abstraction of
continuous color shifts. Indeed, you may have seen that your computer
monitor is capable of 16 million colors! Let's do the math: the cube of
256 is 16.78 million.

HSL stands for hue, saturation and lightness. HSV represents hue,
saturation and value. CMYK represent the printing primary colors of
cyan, magenta, yellow and black. Since most of our work will be done
digitally, then we will focus on the RGB system. The important take away
from this deep dive is that mixing colors differs between pigments and
light. Another idea that arises from this discussion is the importance
of value. We can say that value is a product of mixing colors together.
In the computer this means relative gray values in each of three
channels. For a confirmation of this, check out the three channels of
the color image from a colorful rendering in figure 4.1.2. The red
channel is a monochromatic image. The blue channel is similar but
"highlights" different parts of the image. The green channel is again
slightly different.

\<Insert Figure 4.1.2\>

Figure 4.1.2: Three Monochromatic Channels Make RGB Color Image

Monochromatic values are a fundamental way of discerning pattern
differences. Perhaps second only to the silhouette or outline of an
object, values help us to understand how real-world objects reflect
light. This information yields so much information to the viewer. Since
it is easy to map values that we perceive onto the flat surface of paper
or a viewing screen, then the illustrator can use a value scale to aid
in this coding system. Whereas a computer uses 256 scale values across
several channels, it is often adequate for us to think in only seven
values from black to white. This approximation can be mapped in at least
two different systems, a linear scale and what we'll call here a Lambert
scale. You are recommended to make both scales as rendering practice
ahead of making your Exercise Six. Perspective Projection and Tone Value
Render of a Small Guest House.

\<Insert Figure 4.1.3\>

Figure 4.1.3: Two Grayscale Value Reference Images

#### Photographic Arts as Rendering Paradigm

The development of photography was historically perceived by some as a
threat to painting and even to fine art itself. Artists still paint and
draw now more than ever. Photography has instead become a fine art
itself. Just as electronic modeling and computer rendering is seen by
some as supplanting our need to learn how to draw by hand, what if
architectural illustration is similar to the arc of photography. It is
argued here that photography has improved our capacity to see and
record. It is prudent for the architectural student to develop skills in
all aspects of contemporary practice. That practice can best be
described as a hybrid of several systems.

A paradigm can also be thought of as a model and system. The components
of any system are at least some discrete phenomena we'll call objects
and the interrelationships between these objects. For now, let's keep it
simple. The objects of a rendering are: the represented scene,
transformations from three-dimensional space to two-dimensional
representations, relationships of major and minor representations of
objects as shapes on the *page*, relationships of light reflectance on
the objects and material colors and textures. What is photography to the
architect and illustrator? What does a photographic rendering paradigm
look like? The answer to these questions will be shown as a good
rule-of-thumb or heuristic for our contemporary practices in drawing
that can translate across analog and digital domains.

We are transported back several decades. An architect and photographer
using a single lens reflex (SLR) camera in 1988 visits a project site on
a street corner of a small town. A three-story historical bank will be
renovated into restaurant. In addition to taking photographs to document
the existing conditions, the architect carries a sketchbook, felt-tip
pens and a tape measure. In the camera bag are three *prime* lenses: a
28mm f/1.8, a 50mm f/1.4 and a 105mm f/2.8. Each roll of film is ISO 64
Kodachrome color positive (slide) 35mm film with 36 slides to be
developed by a lab in about one week.

The 28mm lens is effective when taking photographs across the street. It
captures the entire building, although there is a small amount of barrel
distortion that slightly curves the edges of the frame and make the
parallel vertical lines converge to a vanishing point in the sky. This
can either be a useful dynamic view to consider for a rendering later,
or conversely it could be distracting. The illustrator won't know which
until the design idea is considered. The overcast sky makes the light
levels a slight challenge, but this lens is *bright*. Stopping down to
f/4 in these conditions is no problem. Later, when taking photographs
inside, the architect will likely need to use the f/1.8 aperture, and
this will introduce a very shallow depth of field. Again, this
*limitation* can be an attribute or a detraction depending on how the
effect is used creatively.

The 50mm lens most closely resembles our natural field of view that we
see walking around. This will be great for taking exterior shots as
*eye-level* perspective vignettes. These vignettes are so effective at
giving the viewer an experiential quality, so important for making the
project come alive. Again, the even brighter f/1.4 lens will be helpful
for the interior vignettes. All other things being equal the wider the
angle of the lens, then the more light comes through it and is mirrored
onto the film plane. The 28mm allows more light than the 50mm lens, and
the architect is glad for the extra two-third stops available on this
50mm lens. It could mean the difference between getting a low light shot
at 1/30s, which is too hard to hold steady, and 1/60s. Since the
architect forgot the tripod today and must hand hold, that brighter 50mm
will come in very handy!

The 105mm will allow the architect to take detail shots of the
historical cornice. It will help to catalogue the areas where repairs
will be required. No need for a ladder on this trip. These shots can be
taken from the street. It may be useful for the presentation board to
convert some of these images into renderings that demonstrate why the
client should keep the existing cornice for the new design. By the end
of the site visit, the architect has exposed four rolls of film to drop
off at the developer and picked up later that week, hopefully before the
weekend, so that the renderings can be prepared before the client
meeting at the beginning of next week.

Back to the present, you might be asking why did we go into so much
detail about a historical artifact...the 1988 architect and a film
camera? The digital camera mostly has the same physical limitations that
are a function of the glass in the lenses. Further, while these lenses
have been miniaturized to be placed in your phone, the principles remain
the same. And, it turns out, that electronic modeling environments such
as SketchUp, Blender and REVIT use the same terminology borrowed from
photography in setting up the rendered perspective views. While
Kodachrome is almost impossible to find, 35mm negative film stock and
those who can develop it still exist. Used analog cameras are still
available on used markets and lenses are adaptable for both analog and
digital cameras. Does this seem like a good investment or hobby? You
could do worse! It just may help your *eye* for making your renderings.

### Color Models

In the previous section, we discussed at length monochromatic rendering
domains. As you may infer from above, any discussion of grayscale leads
to a discussion of color models too. The physics of four color models
were explored briefly for background. In this section, let's apply this
background to architectural illustration.

#### Tint, Tone and Shade

When you add white to a pure color the result is a **tint** of the
original color. It can appear lighter in tone value. Try not to confuse
this in the digital environment with *opacity*. The confusion arises,
because in a multi-layered image with an underlayer of white, this can
have a similar effect to adding white with pigments. Yes, it is possible
to achieve the same effect this way. It may be better to be more
deliberate in your *color design* by using opacity to blend layers and
by using white color added to some other color to achieve an opaque
tint.

**Tone** in the context of architectural illustration is the relative
lightness or darkness of the pure color. The printing for this book is
monochromatic, and this can make any discussion of color a challenge.
When discussing tone, however, it is ideal for showing the effect in
Figure 4.2. Three pure colors are preproduced in 1-inch (25mm) boxes and
placed side by side. Red when desaturated to monochrome appears as a
little less than 50% gray, or we might say *medium gray* tone. Green
when desaturated is a little more than 10% gray, a *light gray* tone.
Blue when desaturated is about 70% gray, a *medium-dark gray* tone. Each
color has a *natural* or inherent tone in this context. Since we saw
above how important tone-value is to the underlying reading of any
illustration, then by implication we can say that color affects the
tone-value mapping.

**Shade** is the inverse to tint, and black is added to a pure color.
Just as with the discussion above about tint, it is possible to achieve
a similar effect in a digital multilayer environment by changing what is
called the layer blending mode. As you will learn, in *normal* blending
mode, and opaque layer will completely cover up the layer below. If you
change this to *multiply* mode as an example, then it will at once make
the layer seem transparent and darken some shapes in your scene.
Multiply mode is one of our best tools in digital illustration. It is
important to consider this darkening attribute.

As a final consideration, mixing two or more pure colors will affect the
relative tone value mapping as well. The color changes and so too does
the percentage of perceptible tone value. As an example, try this
*formula* in a digital program called GIMP: mix the pure color red on a
top layer set to *LCh* blending mode and a second layer below of pure
blue color also with the LCh blending mode and at the bottom of the
layer stack. The LCh blending mode stands for Lightness, Chroma, and
Hue. This demonstrates both the power of blending modes in a digital
program and the not-so straightforward way colors blend in digital
images. Remember that a red tone was about a 50% gray and a blue tone
was 70% gray. Simple logic might imply that when mixing the two color
tones, a grayscale value somewhere between 50% and 70% might result.
When red is on top, this dark red color has a grayscale value of about
65%. Now, swap the order of the layers and place the blue layer on top.
This new medium violet color has a grayscale value of around 50%! How
did that happen? Layer order matters. Blending mode matters. All
parameters are interactive and not as predictable as we might hope.
Remember: tone value is the most important visual cue after strong
shapes and the silhouette. This implies that when working digitally, it
may be a good idea to periodically create a test layer that combines
your layer structure onto one layer that you can desaturate. If it still
reads effectively in monochrome, then you are on track.

#### Hue, Saturation and Lightness

Let's seek just a little more precision in our language. Tone in
different contexts can mean both a pure color and a color with a gray
color added to it. This ambiguity can be confusing sometimes. Perhaps a
better word is **hue**. Hue is the underlying base color. Looking at the
table for 50% gray above, notice that the value for hue is 0.0. Gray has
no hue. On the other hand, pure red has a value for hue of 0.0 also! In
this context hue is measured in degrees of a color wheel circle. Red is
at 0 degrees. Pure green has a hue value of 120 degrees. Pure blue has a
hue of 240 degrees. Remember from geometry class that in this context
Red could have a value of 0 and 360 degrees, because this circle is
continuous. This implies that as we approach 360 degrees from below and
clockwise or from above and counterclockwise, the hue is approaching the
color red.

**Saturation** in this domain refers to the intensity of a color
relative to pure gray (i.e., 50% gray) in some contexts, and white in
other contexts as we will see. Again, we can use GIMP as our color
laboratory and test our understanding. Start with a pure red by dialing
in the RGB sliders with the following values: Red 255, Green 0 and Blue
0. Select the tab for HSV and grab the "S" slider. It reads 100 and is
pegged to the right side of the scale. While dragging the slider to the
left watch how the color changes and how the values of all the
parameters change. What is the color when dragged all the way to the
left at value 0? It is pure white!

While we are still in GIMP, let's check out what happens when we shift
the **value** scale. Here you can intuit what is meant by value. It is
what we think of as tone-value for our rendering. In the absence of
saturation, we are working solely with value, no matter what our
starting hue was. Continue to shift the sliders at will, and you will
gain a greater understanding of the system and the interactions between
the three parameters of hue, saturation, and value.

### Geometric Transformation Two: Perspective Projection

In chapter three we learned about geometric transformation one:
**parallel projection**. In order to draw the upcoming *Exercise Six.
Perspective Projection and Tone Value Render of a Small Guest House*, we
will need to learn more about perspective projection. Two systems will
be presented here, and one is analog, the other is digital. You will
learn later in this book that these two methods can be combined for the
sake of efficiency. Before we do that, let's discuss the foundational
principles that underly perspective projection.

It is unlikely that you will ever learn the mathematical formula that
underpins perspective projection. For our purposes it is enough to know
there are four inputs. The first input is the three-dimensional (3D)
coordinate position of a point that is projected onto a flat planar
surface. A second input is the 3D position of a "camera." The third
input is the orientation or viewing angle of the camera. Finally, there
is the 3D location of the flat planar surface relative to the camera.
Confused yet? We have learned before that a complex system can be drawn
and diagrammed to provide clarity.

\<Insert Figure 4.3.1\>

Figure 4.3.1: Orthographic Diagram of Setup for Four Perspective Inputs

#### Thumbnail Perspective Method

What may surprise you is that you have a lot of experience working this
complex system out in a more direct method in your head. You probably
are already pretty good at thinking and ultimately drawing in
three-dimensional perspective. What follows is an adaptation of William
Kirby Lockard's "Direct Perspective Method."

> The method put forward here is intended as a lightning-fast freehand
> study method. Rigid drawings are used only to show the method clearly.
> If you get into ticking off and ruling lines you would be better
> actually to project the perspective. It will be more accurate and take
> only a little longer.
>
> Students often take this simple method as a great new all-purpose
> perspective method, and use it to attempt the construction of
> city-scapes, or complex interiors. This is like attempting to play
> Beethoven's Ninth on the harmonica. It is meant to b e a simple,
> relatively accurate, study tool, not a precise technique. (Lockard
> 1977, 16)

The Thumbnail Perspective Method involves at least three drawings. The
method is self-correcting and depends on iterative redrawn perspective
images. Each drawing is progressively larger and builds on a concept of
mapping an architectural space onto an imaginary framework. This is the
kind of book where it is OK to skip around. Please, look ahead to
chapter eight and *Sketch K. Formal Precedent Study. Thumbnail Sketch to
Contour Drawing*. It is important before proceeding to the electronic
modeling method to read through Sketch K, so that you understand the
analog process.

The imaginary framework is very simply stated: you are viewing another
person or persons in front of you who is/are standing in front of and
next to the leading edge (i.e., measuring line) of a cubic volume that
measures ten feet (3 meters) square on all three axes. You are viewing
the cube at an oblique angle, such that one face is more predominant
than the other. This is known as a two-point eye-level perspective.

On a small piece of paper or in the center of your sketchbook draw a
two-inch (50mm) square to mark the bounds of this small thumbnail sketch
drawing. Somewhere near one third from the bottom edge and near one
third of either the right or left side draw a silhouette of a small
human figure, perhaps only ¼" (6mm) high. Draw a horizontal line through
the eyes of your scaled figures and across the page at zero degrees and
label this the horizon line. Assume this is five feet (1.5 m) above the
ground. Double this height using your pencil or pen as a measuring
device, and it yields the height of your cube at the measuring line. The
predominant face of the cube will have a top line and bottom line with
shallow angles that converge probably off the page. The subdominant face
has top and bottom lines with slightly steeper angles that converge. In
the dominant face, estimate that back edge line that *looks* like it
would complete a square. Repeat this process for the subdominant face
and understand that the subdominant back edge will be closer to the
measuring line than the back edge of the predominant face due to
different rates of convergence. If this is confusing, then let's diagram
this together in our sketchbooks.

\<Insert Figure 4.3.2\>

Figure 4.3.2: Thumbnail Perspective Method Setup: Drawing One of Three

Let's call this first drawing a thumbnail. When completed, the cubic
volume will be lightly drawn. As a reference measuring tool, an estimate
of the scene of interest should be drawn to a resolution that clearly
identifies the overall silhouette and additionally the major inner
shapes of the architectural subject. Do not be too concerned if the
proportions of shapes do not match perfectly what you see. We will build
confidence and correction in the second drawing of the trio. The last
step of the first thumbnail drawing is to identify the preferred
compositional framing, presuming that you do not settle on the beginning
square. With a red pen or pencil, lightly divide this compositional
frame rectangle into three horizontal rows and three vertical columns.
Like a muralist, we will use this nine-rectangle grid framework to
transfer our shapes to the larger doubled size of 4"x4" (50mm x 50mm.)

In the second drawing we will redraw with any needed corrections and
seek to resolve the proportioning of the major shapes, add the interior
minor shapes and work on a tone-value shading of the scene in light. It
is your choice to whether to repeat the cubic framework. I would
continue to place human-scaled figures or silhouettes in this second
drawing. The light and shadow study we do here will be intuitive. We
will pick a direction of the light source, the sun, and identify planes
that face toward the light (highlights) away from the light (shades) and
planes that have a cast shadow onto them. This is still a relatively
small drawing and won't allow much detail or texture.

\<Insert Figure 4.3.3\>

Figure 4.3.3: Thumbnail Perspective Method Setup: Drawing Two of Three

The third drawing is in principle very similar to the second. Once
again, we will redraw at a larger size. This time at roughly a 6"x6"
(75mm x 75mm) bounding area. In the preceding drawings we settled on a
composition, and so this bounding area will match the larger of the two
rectangle dimensions. The final drawing should be considered a
rendering. While it is desirable to have very light "lines" to layout
the silhouette, major and minor proportional shapes, our rendering will
make these lines disappear as we solely render the tone-value shapes.
Select either the linear or Lambert tone value scale that we discussed.
Map no more than seven different tone values from black for cast shadows
through middle grays for planes in varying orientations away from the
light source and to a highlight of white. Concentrate on your best
rendering technique that minimizes texture in favor of flat soft washes
of colored pencil.

The preceding three steps are specific to the tone value rendering
method. It is no doubt easy to see how this three-step process would
work for all perspective drawings including a contour line rendering.
The only step that varies for this method is the third rendering step,
which is dependent on your desired result. A color wash as the final
rendering also can apply this direct perspective method.

\<Insert Figure 4.3.4\>

Figure 4.3.4: Thumbnail Perspective Method Setup: Drawing Three of Three

#### Electronic Modeling Method

One of the best tools for three-dimensional visualization is an
electronic digital model. Some of these models can be created very
intuitively and quickly. Others require painstaking and arduously long
hours at the computer. The requirements for selecting one over the other
are often a function of both the stage of the architectural design and
client requirements for a presentation of the design. It is important
for guarding your precious time that you do not fall in the trap of
building a detailed computer model too soon. A much better use of your
time on the computer is to build the very basics of a three-dimensional
framework that allows you to do some previsioning and manipulation of
the model to generate your preferred view. After this very quick
modeling session it can be beneficial to "print" the framework to a
reasonable size on paper and use an overlay technique of tracing paper
refinements like the thumbnail perspective method. While it can be
immensely enjoyable to create new virtual worlds like in a Minecraft
(2021) game, you are well advised to avoid the indulgence of modeling
too much detail and progress quickly to the rendering and visioning
stages of architectural design.

One of the best pieces of advice about electronic modeling you can
follow is the idea to work as "flat" as possible for as long as
possible. What does this mean? Often the designer proceeds from a
two-dimensional multi-view orthographic drawing such as a plan, section,
or elevation. Working flat is the process of drawing rectangles, lines,
and shapes without a "Z" dimension. This process is useful because most
electronic modeling programs are *sticky* and ambiguous in the
representation of depth! What does that mean? Geometries are welded
together at vertices. When you try to move a line segment to a new
position, it can have many unintended stretching consequences.
Additionally, when we view space from a non-orthographic *perspective*
our relationship to the depth that we see may be intuitively obvious to
us, and the computer does not share our intuition. The software
developers have embedded inferences about intersecting geometries that
can sometimes be helpful. On the other hand, it can be exceptionally
frustrating when the computer gets it *wrong*! Therefore, work for as
long as possible while managing only two dimensions. When it is time to
push and pull your geometries into the z-axis, then it will be an
exceptionally satisfying experience. But wait...there's another thing to
do before that.

Since geometries tend to be joined at vertices resulting in unintended
stretching, each program you will encounter has some method of grouping
elements together into systems. You are well advised to be profligate in
your use of these groups. This is powerful modeling, and the pros make
excellent use of this kind of *templating* of components. The following
table is a guide to some common terminology for you to research and
learn the basics of making groups or components:

  -------------- ------------------
  Program Name   Element Name
  AutoCad        Block
  REVIT          Family
  SketchUp       Group, Component
  Blender        Group
  Maya           Group
  -------------- ------------------

Here are some final thoughts about the electronic modeling method. It is
much easier to create any view that you desire, and this can have some
unintended consequences. Extreme perspective distortion can be very
exciting, and when it is not a deliberate choice of the designer, it can
also be very distracting to your focus on the design. Here are a few
reminders from an earlier discussion about photography. Our most
frequent view of an object is from a standing eye-level perspective,
usually about five feet (1.5 meters) above the ground and with a 50mm
lens. This view will challenge you, because it often does not allow you
to include *everything* that you have modeled. Maintaining this view is
a good discipline, and if you are wanting to show more distortion, then
have a very good reason for that view and be deliberate in your purpose
(e.g., contrast, tension, dynamics, juxtaposition, etc.) Additionally,
use the computer as a tool. Model only the bare basics of what you need
for the purpose. As an example, in the next assignment you will be asked
to model a guest house electronically. Our main purpose here is to use
the computer as a tool to define and *design* the sun and shade
patterns. You only need the basic cubic volumes. No materials are
needed. No textures are needed. This is often referred to as a clay
model rendering, which owes its namesake to the physical modeling
material clay. Two main advantages come from this decision to be
minimalistic in your approach: it takes far less time for you to model,
and it takes far fewer resources for the computer to render the desired
image. Always remember that the goal is a tone value rendering. The
software can make this task both harder and easier. The choice is yours!

## Exercise Six. Perspective Projection and Tone Value Render of a Small Guest House

### Introduction

A "perspective" is a non-orthographic three-dimensional drawing, and the
view often resembles what we observe and can photograph. The perspective
view we are going to draw uses an electronic model method, which can be
contrasted to a mathematical analog method we will learn later. In a
perspective, parallel lines converge to vanishing points. These drawings
are useful throughout all phases of the visualization process of design
and are easily constructed using varying methods.

\<Insert Figure 4.4\>

Figure 4.4: Exercise Six. Perspective Projection and Tone Value Render
of a Small Guest House

### Learning

This assignment module contributes to the following design learning
outcomes, which finish the sentence "As a successful student in this
course, I am now able..."

-   ... to analyze a field sketch of a built environment condition and
    synthesize that information by modeling the conditions in a
    three-dimensional visioning program.

-   ... to transform parameters within an electronic computer model and
    simulate the influence of highlight, shade, and shadow.

-   ... to visualize the built environment in a tone-value rendering
    using dry media techniques.

As mentioned in Exercise Five Axonometric Projection Contour Model of a
Small Guest House, electronic modeling is an attractive and fun drawing
to make. It may take a significant amount of time to model every screw.
Thankfully, we only need to model the major forms of our guest house.

> Modeling with exact dimensions...is the best method.... You need to
> determine the level of detail that should be included in your
> models.... Excessive detail is usually unnecessary, and it will slow
> you down. (Brightman 2013, 332--33)

A tone-value rendering maps shapes to at least three types: highlights,
shades, and shadows. Since tone-value is an important visual cue that
allows us to understand the representation of a three-dimensional object
on a two-dimensional surface, then it is a valuable image to describe
the form of an object. The relationships between light and dark are well
understood by the viewer because one encounters the interplay of light
and dark shapes on objects due to the influence of a light source, such
as the sun. This illusion works well unless the tone-values are
ambiguously mapped and show too little clear distinctions between the
implied planes. Therefore, when translating from observed
three-dimensional phenomena onto a two-dimensional surface, artists and
illustrators can confidently convey the shared experience we have moving
around in space and interacting with visual objects.

> The value key or tonality...is the first impression received and
> immediately engenders an emotional reaction irrespective of the
> subject matter or composition. It must be remembered that we react to
> light in a very primitive manner...the intensity of light reflected to
> the eye determines the primary emotional response. White, gray, or
> black surfaces reflect varying amounts of light, each creating a
> distinctly different mood in the observer. (Graves 1941, 129)

### Materials

-   Colored pencil (i.e., black.)

-   Trimble SketchUp

-   12x18 (305mm x 457mm) sheet

### Steps

1.  Begin by creating a simple model in SketchUp.

2.  Construct the model from the sketch provided and position the final
    point of view looking at the same corner as the sketch.

3.  Setup the shadow positions within the model to provide the most
    aesthetically pleasing interplay of sun-shade-shadow composition.

4.  After completing the model, print to letter-sized paper at a size
    roughly equivalent to your other drawing.

5.  Lay the 12"x18" (305mm x 457mm) vellum sheet over the printed model
    and render with a black colored pencil, using a tone-value method
    (i.e., no line work allowed!)

### Criteria

  DLO               Advanced (4 pts)                                                                                                                                                                                                                                  Proficient (3 pts)                                                                                                                                                           Developing (2 pts)                                                                                                                                                         Beginner (1 pt)                                                                                                                               
  ----------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------- --
  Craft             Illustrator demonstrates exemplary attention to work product and excellence.                                                                                                                                                                      Illustrator demonstrates good attention and care towards work product.                                                                                                       Illustrator completes work, but the product seems rushed to completion.                                                                                                    Illustrator demonstrates attention towards work product, but work quality is                                                                  
  Rendering         Illustrator uses tone value to represent the interplay of light on volumetric forms. Image is controlled and evokes both power and subtlety. Image is descriptive and/or symbolic and supports compositional goals.                               Illustrator\'s tone value work demonstrates several professional attributes. Rendering style does not distract the viewer and generally supports compositional objectives.   Illustrator\'s use of tone value is somewhat effective. Rendering style is consistent and competent. There are some non-contributing attributes.                           Illustrator attempts to use tone value descriptively. Rendering is inconsistent and lacks attention to craft.                                 
  Technical         Modeler observes and analyzes object data and translates it to a meaningful electronic model representation. Professional conventions are followed, inclusive of view selection, accurate translation of field notes and light source selection   Modeler observes and analyzes object data and translates it to a meaningful electronic model. Most professional conventions are followed, and some information is missing.   Modeler is challenged to observe and analyze field sketch correctly in the electronic model. Few professional conventions are followed, and some information is missing.   Modeler attempts to observe and analyze field sketch and representation is inconsistent. Professional drawing conventions are not followed.   
  Professionalism   Student completes the work on time. Work demonstrates exemplary attention to learning objectives.                                                                                                                                                 Student completes the work on time and demonstrates a good work ethic.                                                                                                       Student generally completes the work at a minimum level of expectation.                                                                                                    Student is missing parts of the work and makes a plan for completion of the remaining assignment.                                             

### Related Assignments

-   Sketch D. Field Sketches of Two Exterior Elevations of Large
    Buildings

-   Exercise Five. Axonometric Projection Contour Model of a Small Guest
    House

-   Exercise Seven. Interior Construction Drawing. Floor Plan and
    Interior Elevations

### References

Brightman, M. 2013. The SketchUp Workflow for Architecture. Hoboken, NJ:
John Wiley & Sons, Inc.

Graves, M. 1941. The Art of Color and Design. First. NY: McGraw-Hill
Book Company, Inc.

Lockard, W.K. 1977. Drawing as a Means to Architecture. Pepper
Publishing. Tucson, AZ.

Minecraft Official Site. 2021. Minecraft.net.
<https://www.minecraft.net/en-us>.