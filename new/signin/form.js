function findLocation() {
                const result = document.getElementById('locationResult');
                    if (navigator.geolocation) {
                        navigator.geolocation.getCurrentPosition(
                            (position) => {
                                result.textContent = 
                                     `Latitude: ${position.coords.latitude}, Longitude: ${position.coords.longitude}`;
                            },
                            () => {
                                 result.textContent = "Unable to retrieve your location.";
                     }
                );
            } else {
                result.textContent = "Geolocation is not supported by your browser.";
            }
        }