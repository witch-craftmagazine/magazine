{% extends "base.tpl" %}

{% block content %}
<div id="musicbox-container" style="max-width: 800px; margin: 20px auto; padding: 15px; text-align: center;">
    <h1 id="page-title">{{ page_title }}</h1>
    <p>Tune in to the melodic spells and rhythms of Deathcap Island.</p>
    <div style="width: 100%; height: 600px; position: relative; margin-top: 20px;">
        <iframe src="https://open.spotify.com/embed/playlist/03YJoI5Wbu2tEXu27VFAeR?utm_source=oembed" 
                style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0; border-radius: 12px;" 
                allowfullscreen="" 
                allow="clipboard-write; encrypted-media; fullscreen; picture-in-picture;" 
                loading="lazy">
        </iframe>
    </div>
</div>
{% endblock %}
