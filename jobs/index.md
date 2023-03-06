# Jobs at U.S. Medical Universities & Big Pharma Companies

> Scraped and aggregated from official websites

{::options parse_block_html="true" /}

<div id="map"></div>

{% assign jobs = site.data.jobs | sort_natural: "Company" %}
<table>
{% for row in jobs %}
    {% if forloop.first %}
    <tr>
        {% for pair in row %}
            {% assign key = pair[0] %}
            {% assign value = pair[1] %}
            <th>{{ key }}</th>
        {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
        {% assign key = pair[0] %}
        {% assign value = pair[1] %}
        {{ value }}
    {% endtablerow %}
{% endfor %}
</table>
