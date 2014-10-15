            // Create map object with Leaflet
            var map = new L.Map('map', {
                zoomControl: false,
                center: [43,0], // Southern France
                zoom: 5
            });
            
            // Add OpenStreetMap tiles
            L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: 'OpenStreetMap'
                }).addTo(map);

            vzj = 'http://documentation.cartodb.com/api/v2/viz/2b13c956-e7c1-11e2-806b-5404a6a683d5/viz.json';


            cartodb.createLayer(map,vzj).addTo(map);
            // var vizjsons = [
            //     'http://documentation.cartodb.com/api/v2/viz/2b13c956-e7c1-11e2-806b-5404a6a683d5/viz.json',
            //     'http://documentation.cartodb.com/api/v2/viz/236085de-ea08-11e2-958c-5404a6a683d5/viz.json'
            //     ]

            // vizjsons.forEach(function(vizjson, index) {
            //     cartodb.createLayer(map, vizjson)
            //         .addTo(map)
            //         .done(function(layer) {
            //             alert("Congrats, you added vizjson #" + (index+1));
            //         })
            //         .error(function(err) {
            //             console.log("error: " + err + " for layer " + index);
            //         });
            //     });
