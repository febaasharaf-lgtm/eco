function getRecyclingCenters(location) {
    const mapsUrl = `https://maps.googleapis.com/maps/api/place/textsearch/json?query=recycling+centers+in+${location}&key=YOUR_API_KEY`;
    
    fetch(mapsUrl)
        .then(response => response.json())
        .then(data => {
            const centers = data.results;
            let centersList = "<h3>Nearby Recycling Centers:</h3><ul>";
            centers.forEach(center => {
                centersList += <li>${center.name} - ${center.vicinity}</li>;
            });
            centersList += "</ul>";
            document.getElementById("recyclingCenters").innerHTML = centersList;
        })
        .catch(error => console.error("Error fetching data:", error));
}
  
 