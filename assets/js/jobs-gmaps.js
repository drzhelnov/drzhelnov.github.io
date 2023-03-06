let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: new google.maps.LatLng(37.6, -95.665),
    zoom: 4,
  });

  const features = [
    {
      position: new google.maps.LatLng(37.6, -95.665),
      title: "sfgsdfg",
      description: "<a href=\"https://careers.duke.edu/search/\">hello there</a>"
    },
    {
      position: new google.maps.LatLng(37.6, -96.665),
      title: "wgwgqrg",
      description: "obi wan kenobi",
    },
  ];

  // Create markers.
  for (let i = 0; i < features.length; i++) {
    const marker = new google.maps.Marker({
      position: features[i].position,
      title: features[i].title,
      map: map,
    });

    const infowindow = new google.maps.InfoWindow({
      content: features[i].description,
      ariaLabel: features[i].title,
    });

    marker.addListener("click", () => {
      infowindow.open({
        anchor: marker,
        map,
      });
    });
  }
}

window.initMap = initMap;
