---
date: 2023-06-13
slug: 2023-06-dividing-city-race-restrictive
tags:
- legacy-blogger
title: 'Dividing the City: Race-Restrictive Covenants in St. Louis and St. Louis County'
---

# Dividing the City: Race-Restrictive Covenants in St. Louis and St. Louis County

:fontawesome-solid-user: By Colin Gordon & Jay Bowen 

Featured Item or Collection: [Dividing the City][1] 

## What is the item?

These items feature data on covenant restrictions in St. Louis. They are part of an effort to document the spatial distribution and extent of a mechanism widely understood to be a root cause of ongoing racial segregation and wealth inequality. They make visible these efforts to maintain racially divided access to property and wealth, which were long concealed in the extended pages of local records. 

<!-- more -->

## What BTAA Library submitted the item?

University of Iowa 

## Interesting tidbits

* An outgrowth of the Mapping Prejudice project initiated at the University of Minnesota
 * The uneven digitization of property records including racial restrictions presented unique impediments to reproducing the research in Greater St. Louis, Missouri
 * The expansion of private racial restrictions in the St. Louis region were mapped from the late nineteenth century to their decline with _Shelley v Kraemer_ in 1948
 * Mapping this quantity of data in interactive format also presented issues with responsiveness that were solved by converting the geojson polygon data to vector tiles
 * Such restrictions calcified notions about racial homogeneity and property value in US cities that have continued to impact educational opportunity, economic mobility, and intergenerational wealth Inspired by the work of researchers and community activists in Minneapolis ([Mapping Prejudice][2]) and Seattle ([Segregated Seattle][3]), we set out to document the use of racial restrictions on property in St. Louis in the first half of the 20th century. Such restrictions are widely understood to constitute the root cause of racial segregation and lasting disparities in racial wealth, and the foundation of local and federal policies that succeeded them. And yet, because the restrictions themselves are buried in local property records, they have proven difficult to document. 

[![][image-1]][4]{ width="300" }

 [St. Louis Deed Book 1121-525 (1893), p3.][5] 
 
In some settings (including Minneapolis), the digitization of records has enabled "distant reading" through optical character recognition. In St. Louis City and St. Louis County, however, the records are unevenly digitized and—for the era of private restriction—largely handwritten. So we needed a different research strategy. We were able to exploit a wrinkle in local recording conventions: In Missouri, as in a few other settings, county recorders not only documented restrictions in individual deeds, but also required developers and realtors to file "master agreements" covering entire subdivisions or neighborhoods. In both St. Louis and St. Louis County, such agreements are filed with a regular run of deed records or plat maps. Additionally, they are indexed separately from the "grantor and grantee" index that otherwise governs the organization of deed books. In St. Louis City, this was by one of the local title companies; in St. Louis County, this was by the recorder themselves. 

[![][image-2]][6]{ width="300" }

 [Crestwood (1928), Plat Book 26-25][7] 
 
 In each jurisdiction, we collected the effective date, language, terms, and scope of each restrictive indenture or agreement. Using the current county assessor or recorder shapefile of property parcels, we used stable legal descriptions (common to historical and current records) to match historical restrictions to current parcels. This enabled us to map the trajectory and reach of private racial restrictions, from their earliest iterations in the late nineteenth century, through the explosion of their use in response to the First and Second Great Migrations (especially during the housing boom of the 1920s), to the abrupt decline in the practice after the Supreme Court decision in _Shelley v Kraemer_ (1948). 

[![][image-3]][8]{ width="300" }

 [Racial Restrictions in Greater St. Louis, 1870 - 1952][9] 
 
 Starting from these linked data in shapefile format, we endeavored to build an interactive map of the nearly 100,000 restricted parcels in St. Louis and St. Louis County. Mapping such a large quantity of data proved initially to be a challenge. Early efforts at producing an interactive map using Leaflet JS to pull from large files in GeoJSON format resulted in slow loading and sluggish map responsivity to the interactive elements, like the time slider, hover-activated tooltip, layer control, and zoom button. To avoid having to separate the map into city and county partitions, we opted to convert the GeoJSON data into vector tiles and handle the resulting tile set with another open-source map-oriented JavaScript library, MapLibre GL JS. With vector tiles, the map can shed unseen data and simplify polygons at smaller map scales. This allowed us to plot the full collection of restricted private parcel data without crashing the application, thereby providing the public with an uncomplicated visual account of racial segregation in Greater St. Louis that would otherwise remain concealed in overwhelming volumes of handwritten deeds and subdivision agreements. 

[![][image-4]][10]{ width="300" }

 [Real Estate Advertisement Promoting "Careful Restrictions" and "Desirable Neighbors"][11] 
 
These private restrictions were an important source of segregation and housing occupancy in their own right, setting the terms of racial occupancy in northern and border cities across a half century of dramatic urbanization and migration. It also served as the foundation for durable inequalities. In part, this was because its base assumptions—about property values, land use, and neighborhood homogeneity—were emulated and entrenched by local zoning and federal housing policies. In part, this was because, in the American context especially, so much else—including educational opportunity, economic mobility, and intergenerational wealth—flowed from those housing investments. Our St. Louis research is hosted as the digital project "[Dividing the City][12]" by the University of Iowa Digital Scholarship and Publishing Studio, and the mapping resources are mirrored by our community partner, the [Equal Housing and Opportunity Council of Metropolitan St. Louis][13]. For a digest of ongoing projects around the country, see the [National Covenants Research Coalition][14]. 

## Where can I find out more?

* To see the full project as well as further explanation of Dividing the City: Race-Restrictive Covenants in St. Louis and St. Louis County, you can view the website [here][15]
 * To see the code behind the map, please go to this [GitHub repository][16]
 * To see an explanation of how to generate custom vector tiles and map them with Maplibre GL JS, please read the instructions [here][17]
 * To see recent press about this project, you may view the list of links [here][18] Colin Gordon, Department of History, University of Iowa Jay Bowen, University of Iowa Libraries, University of Iowa.

!!! note ""
 
	This was originally posted on blogger [here](https://geobtaa.blogspot.com/2023/06/dividing-city-race-restrictive.html).


[1]:	https://geo.btaa.org/catalog/b492921b-eebf-442f-acb4-1dc6b0d21cc8
[2]:	https://mappingprejudice.umn.edu/ "https://mappingprejudice.umn.edu/"
[3]:	https://depts.washington.edu/civilr/segregated.htm "https://depts.washington.edu/civilr/segregated.htm"
[4]:	https://blogger.googleusercontent.com/img/a/AVvXsEgD_96fEJgtwFXCzyXmxDUDHQDzkzDQla01Y6MTQPmDNMncYhqVSwCXCd75wKJmhZsK80GwDJZJ52-s8886nYij4FLCbTLOSQDf9XSNeiO4CjcQpu0-JniYlF6Xn1GhRBQW0CKkHVi9xlhqsmYqpB6-B6vdRKUY3hfSG2nNk8Pus2hacXpSOiPxmofHjQ
[5]:	https://dsps.lib.uiowa.edu/thedividedcity/wp-content/uploads/sites/94/2022/05/1893c-Minerva-Ave-1024x768.jpg "https://dsps.lib.uiowa.edu/thedividedcity/wp-content/uploads/sites/94/2022/05/1893c-Minerva-Ave-1024x768.jpg"
[6]:	https://blogger.googleusercontent.com/img/a/AVvXsEhz2cy74SqlsXuU3fYAeAC-KJRUSsj56vAt0ck8MbrfJWfUQjtzUPJgVYVlQ7W79AckectkJPNBbs7dqEISwWuG4cRGedQk8-nqW-EPQY9ghyn_k7qkI84otY3h1VvgXWq7u1gFnp4Z7cLnO8_rkHLiVhvL2n6w3R-IC5ZXsqWH_2ttbP8wErZMI9MSmA
[7]:	https://dsps.lib.uiowa.edu/thedividedcity/wp-content/uploads/sites/94/2022/05/PB-26-25-Crestwood-2d-Add-scaled.jpg "https://dsps.lib.uiowa.edu/thedividedcity/wp-content/uploads/sites/94/2022/05/PB-26-25-Crestwood-2d-Add-scaled.jpg"
[8]:	https://blogger.googleusercontent.com/img/a/AVvXsEhjs-BFni8TqphYu4TBvsUV45qZpGXg1jYt6fUdUdNiRQEE4RlpTcd0FtiROX3dtTBNBrGHvv-9Sncz9u7FwPupr4bxlT4F9vTR_j2zTzBXgxIudXTRZlgZ2hWPIm7Q_UnIdCnsjZcY2mXDnjPhRKa3tZzBT2hjCkydbvhG86MuUFIFQ-sF_1Su8vxzHA
[9]:	https://dsps.lib.uiowa.edu/thedividedcity/map/ "https://dsps.lib.uiowa.edu/thedividedcity/map/"
[10]:	https://blogger.googleusercontent.com/img/a/AVvXsEjlnVy2bcHpEkGfBe1QTXXhy4c5fSMQUz0wbeHYzvd6IUSCfVzEbw5P94Zqr68iiQQ3r6jeAJp4DGdknSpifb-d1GOR67htJql8QgIATM2VgwLACNG5NRiIxPBX9Omedb05zDSq_ynMticP9hcp_UKXJwTnYIJpYBGgPgKNoCxVOZ-ZaF_XQCArZakLNQ
[11]:	https://dsps.lib.uiowa.edu/thedividedcity/wp-content/uploads/sites/94/2022/05/Hampton-Park-1910.jpg "https://dsps.lib.uiowa.edu/thedividedcity/wp-content/uploads/sites/94/2022/05/Hampton-Park-1910.jpg"
[12]:	https://dsps.lib.uiowa.edu/thedividedcity/ "https://dsps.lib.uiowa.edu/thedividedcity/"
[13]:	https://ehocstl.org/restrictive-covenants/ "https://ehocstl.org/restrictive-covenants/"
[14]:	https://www.nationalcovenantsresearchcoalition.com/ "https://www.nationalcovenantsresearchcoalition.com/"
[15]:	https://dsps.lib.uiowa.edu/thedividedcity/
[16]:	https://github.com/ui-libraries/greater-st-louis-covs
[17]:	https://github.com/jebowe3/maplibre-gl-js-demo
[18]:	https://dsps.lib.uiowa.edu/thedividedcity/press/

[image-1]:	https://blogger.googleusercontent.com/img/a/AVvXsEgD_96fEJgtwFXCzyXmxDUDHQDzkzDQla01Y6MTQPmDNMncYhqVSwCXCd75wKJmhZsK80GwDJZJ52-s8886nYij4FLCbTLOSQDf9XSNeiO4CjcQpu0-JniYlF6Xn1GhRBQW0CKkHVi9xlhqsmYqpB6-B6vdRKUY3hfSG2nNk8Pus2hacXpSOiPxmofHjQ=s320
[image-2]:	https://blogger.googleusercontent.com/img/a/AVvXsEhz2cy74SqlsXuU3fYAeAC-KJRUSsj56vAt0ck8MbrfJWfUQjtzUPJgVYVlQ7W79AckectkJPNBbs7dqEISwWuG4cRGedQk8-nqW-EPQY9ghyn_k7qkI84otY3h1VvgXWq7u1gFnp4Z7cLnO8_rkHLiVhvL2n6w3R-IC5ZXsqWH_2ttbP8wErZMI9MSmA=s320
[image-3]:	https://blogger.googleusercontent.com/img/a/AVvXsEhjs-BFni8TqphYu4TBvsUV45qZpGXg1jYt6fUdUdNiRQEE4RlpTcd0FtiROX3dtTBNBrGHvv-9Sncz9u7FwPupr4bxlT4F9vTR_j2zTzBXgxIudXTRZlgZ2hWPIm7Q_UnIdCnsjZcY2mXDnjPhRKa3tZzBT2hjCkydbvhG86MuUFIFQ-sF_1Su8vxzHA=s320
[image-4]:	https://blogger.googleusercontent.com/img/a/AVvXsEjlnVy2bcHpEkGfBe1QTXXhy4c5fSMQUz0wbeHYzvd6IUSCfVzEbw5P94Zqr68iiQQ3r6jeAJp4DGdknSpifb-d1GOR67htJql8QgIATM2VgwLACNG5NRiIxPBX9Omedb05zDSq_ynMticP9hcp_UKXJwTnYIJpYBGgPgKNoCxVOZ-ZaF_XQCArZakLNQ=s320