---
date: '2022-03-23'
slug: 2022-03-the-ripple-effect-of-interface-change
tags:
- interface
- legacy-blogger
title: The Ripple Effect of an Interface Change
---

# The Ripple Effect of an Interface Change

:fontawesome-solid-user: By Danny Dotson 

![](https://lh3.googleusercontent.com/rDmrHBzZpXbHe-L55ZQUk02AdMOlCEZ_S_Kt9Pq2U2C715oQ81ke8PH0x0RdxcgAUaqqoN0mrrpoeAP-SJY0bEZMUUWwD1vd7HFpS9I3ZVx2aGtIAz3jgCda8x32ZozWKl2oMIpn)

Source:[ EPA](https://www.epa.gov/sites/default/files/2019-08/documents/2012-guidelines-water-reuse.pdf) 

One of the features the Interface Committee has heard that would be useful for the Geoportal to have is the ability to either search for or filter by language. <!-- more --> So fine, let's make that happen. But, this is going to cause work in other areas to make language searching/filtering actually work well. Why is this the case? 

### Metadata: Does Each Item Have a Language listed? 

Short answer: no. So this means for language to be a valuable search/filter option, items need to have a language included in their metadata. Many currently don't. Most of these are very likely in English as they are geospatial data sources from various government entities in the US. But until we make sure and the change is made, the language for these items is essentially non-existent. So the people working with metadata would need to examine the language-less items to add the appropriate language to the item's metadata. This can be time consuming just because of the volume of items. But also, some items may be in a non-English language, but would the person looking at it know what that language is? So this is a lot more complicated than "Look. Add Language. Look. Add Language….." It's more like "Look. English. Look. English. Look. What is that? Help!" 

### Collections: Should we add new content based on language? 

If we have language search/filter options, this gives us incentives to be sharing more diverse collections in terms of language. Are there strong non-English languages' collections for print maps? Perhaps we should be adding collections of Japanese maps, which have a few institutions with over 1,000 maps. Or should we look at maps with languages that are in the single digits to showcase some of our rarer languages? This creates work for our Collections folks. But of course, has implications for Metadata. 

### Application Development 

Of course, the people working on the development of our interface would need to be involved in order to make the language search/filter option happen. But how they need to do it has implications for metadata. So the moral of this story is that by just making one addition or change to the interface, even if it's deemed valuable, it can have a ripple effect of making work for others or opening up the possibility for new projects (and thus, more work). 

!!! note ""

	This was originally posted on blogger [here](https://geobtaa.blogspot.com/2022/03/the-ripple-effect-of-interface-change.html).

