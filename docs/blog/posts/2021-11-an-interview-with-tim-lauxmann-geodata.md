---
date: '2021-11-03'
slug: 2021-11-an-interview-with-tim-lauxmann-geodata
tags:
- data provider interview
- michigan
- legacy-blogger
title: An interview with Tim Lauxmann, Geodata Data Manager, State of Michigan Department
  of Technology, Management & Budget, Center for Shared Solutions
---

# An interview with Tim Lauxmann, Geodata Data Manager, State of Michigan Department of Technology, Management & Budget, Center for Shared Solutions

:fontawesome-solid-user: Interviewer: Kathleen Weessies

This interview is part of our Data Provider Series, which highlights local governments and institutions that offer open GIS data. In each interview, providers tell us about their missions and data resources. We hope this will be a great way for readers to learn more about local GIS developments and new initiatives. 

* Name: Tim Lauxmann 
* Title: Geodata Data Manager 
* Employer: State of Michigan Department of Technology, Management & Budget, Center for Shared Solutions Website: [https://www.michigan.gov/gis](https://www.michigan.gov/Fgis&sa=D&sntz=1&usg=AFQjCNE1KtJDxOc5kQ1baTg0u3mvo7RpjQ) 
* Open Data Portal: [https://gis-michigan.opendata.arcgis.com/](https://gis-michigan.opendata.arcgis.com/F&sa=D&sntz=1&usg=AFQjCNE0be1cQRcfajUcqAYsq0TL5bbd3w)

<!-- more -->

## What is the mission of your organization? 

The State of Michigan’s Center for Shared Solutions (CSS) provides enterprise governance and delivery of services & products that are common to areas within state government. CSS also manages partnerships with local governments, educational institutions, and not-for-profits to leverage technology efficiencies across traditional organizational boundaries. My unit, Geospatial Services, provides GIS-related database management and support, GIS applications and application support, consulting services, and manages ESRI licensing to state agencies. We also collaborate heavily with local agencies & governments in Michigan and the U. S. Census. To a certain degree, we are also engaged in public outreach. I manage the Geodata Team, which is part of Geospatial Services. We maintain the Michigan Geographic Framework (MGF) and manage the Open Data Portal. My team also provides geospatial consulting and support, specialty mapping and geocoding services, creates and maintains apps for state agencies and programs, works with local agencies, and provides boundary updates for the Census. For this post, we focus on the Michigan Geographic Framework. From its inception in 2000 and through MGF version 17, updates to the framework were made annually. We are currently working on the next generation MGF (version number to be decided, but let’s say v21), which will be something entirely different. While the prior versions were static and updated annually, the new MGF will be dynamic. The Guiding Principles for the Michigan Geographic Framework Geospatial Data Hub:

 * Create data once, use many times
 * Data from authoritative sources
 * Data classification by data owners
 * Regular data updates and maintenance
 * Effective metadata
 * Partnerships and data sharing agreements
 * Consistent data for decision making – local, state, federal, public 

## How do you create the geospatial data? 

The Michigan Geographic Framework is a hub of data that receives files from our data partners, such as other state agencies, the federal government, and Michigan county governments. MGF incorporates the processing power of the 1Spatial production engine to ingest authoritative GIS data from the data steward for that data. For example, our biggest data contributor is the Michigan Department of Transportation (MDOT). As they have updates ready, they upload their linear reference systems (LRS) data through the portal we established for them. The 1Spatial engine processes datasets according to established business rules and incorporates them into MGF. After the initial upload, subsequent updates will only process areas identified during a change detection process and identify differences from what is already in the MGF. The process is complicated by the fact that there will be more than one contributor uploading the same type of authoritative data. In this case, local contributors (county level) will also be contributing road data. The 1Spatial business rules ensure that the data from the different contributors is processed such that we maintain one centerline. In the case of MDOT and local roads, MDOT geometry on any road that is in their LRS takes precedence over the local geometry. Conversely, local road attributes, such as the primary street name (i.e., what shows up on the street sign) and address ranges (which MDOT does not maintain but are essential for emergency services), are added to the attribute tables. This is just one example, but it illustrates how 1Spatial uses the MGF business rules to ensure data standards are maintained. 

[![MDG Data Hub - Data Flow](https://blogger.googleusercontent.com/img/a/AVvXsEiOBumxoskUea3Ytvzl7FFkDMGPDufiGjtZF7itghAqz7k9jnPvy8KO73aUbrOkcXiGpKQfe4xJGe77R7Ys2BmEHn5wNnUc2ts398dkMu_madKU8kzZrv88Rt2rY1_wMlfM8aw5ebB7kfMSKI8KiisXwhbysjjzXa2nReBC3fE67MDPsx7R9AwRyDYQzA=w640-h360)](https://blogger.googleusercontent.com/img/a/AVvXsEiOBumxoskUea3Ytvzl7FFkDMGPDufiGjtZF7itghAqz7k9jnPvy8KO73aUbrOkcXiGpKQfe4xJGe77R7Ys2BmEHn5wNnUc2ts398dkMu_madKU8kzZrv88Rt2rY1_wMlfM8aw5ebB7kfMSKI8KiisXwhbysjjzXa2nReBC3fE67MDPsx7R9AwRyDYQzA=s1280){ width="300" }

Guiding principles of MGF Geospatial Data Hub, example 1.

## How are your geospatial datasets distributed? 

Some datasets are sensitive in nature and are only accessible to qualified users who are subject to non-disclosure agreements. These are generally people at various state agencies or other government entities. Other datasets are made freely available at the Michigan Open Data Portal. Traditionally, MGF has made data available by exporting layers to our Open Data Portal. Some of this data is accessible to the public, and some requires permission to access. Some of the data we maintain is restricted, such as the PSAP (Public Safety Answering Points) data used by emergency services. The process of exporting to the Open Data Portal will continue. However, with the new MGF, after a contributor’s data is ingested and incorporated into MGF, specialty maps will be available to our partners through the MGF Publication Portal. In line with the idea of ‘create data once and use many times,’ this means that geospatial products will be produced based on the specific requirements of the requester. 

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjZ2N4M0_l5Hf5e9ONI2xq3X4c6FWdbJ9XuGSxPr1r_2apSdUGFbKz2-MAgGs3JhSOqNZKdNZb2J6u2lKfvAHedxif01QD1EZCUhDje3lX-z7Pe5_jDfnP_KOy5p2ShJjbYXRuBfWGc1IUIZ_MOIi40HrxEjIczsvI7J9FO4P0zznkNcJ3ZfPpg6ujJTg=w640-h360)](https://blogger.googleusercontent.com/img/a/AVvXsEjZ2N4M0_l5Hf5e9ONI2xq3X4c6FWdbJ9XuGSxPr1r_2apSdUGFbKz2-MAgGs3JhSOqNZKdNZb2J6u2lKfvAHedxif01QD1EZCUhDje3lX-z7Pe5_jDfnP_KOy5p2ShJjbYXRuBfWGc1IUIZ_MOIi40HrxEjIczsvI7J9FO4P0zznkNcJ3ZfPpg6ujJTg=s1280){ width="300" }

Guiding principles of MGF Geospatial Data Hub, example 2.

## Who typically requests your geospatial datasets, and how are they used? 

We receive requests from partnering organizations and from researchers outside of government. We work collaboratively with many agencies to customize data outputs that they need to carry out their missions. One interesting example of the unique data needs of various government agencies is the complicated nature of political boundaries and how they affect elections and voting. Local governments can gain land by way of the annexation process. But Michigan has an unusual temporary variation known as a ‘425’ annexation. This can mean that land belongs to a unit of government for a period of 25 or even 50 years, then might revert back to a rural township. These agreements must be tracked carefully so that voters in those areas are assigned to the correct voting precinct. Within the wording of the annexation agreement (whether regular or 425), the disposition of voters is specified. This disposition is important to the Bureau of Elections because voting precinct boundaries can’t extend outside municipal boundaries. On the other hand, for others, such as MDOT’s Act 51 program and the Census Boundary and Annexations Program (BAS), what is important is the change to the municipal boundary, not the disposition of the voters. To juggle these needs in the past, my team maintained two sets of boundary data. With the new MGF, we will have one set of boundary layers and use attributes to output the required data for each stakeholder. Check out more data from the State of Michigan in the [BTAA Geoportal here.](https://geo.btaa.org/catalog%3Ff/55Bpcdm_memberOf_sm/55D/55B/55D%3D06a-01&sa=D&sntz=1&usg=AFQjCNHSdcrGJsi_ck92cK7bnwYRHmL2qA) 

!!! note ""

	This was originally posted on blogger [here](https://geobtaa.blogspot.com/2021/11/an-interview-with-tim-lauxmann-geodata.html)*.

