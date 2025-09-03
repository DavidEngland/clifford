# Spacetime Dilation Calculator for Science Fiction

This interactive calculator helps screenwriters determine how time dilation affects characters traveling at high speeds through space. Simply save this entire document as an HTML file to use the calculator locally.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sci-Fi Spacetime Dilation Calculator</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #0a1929;
            color: #e0e0e0;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #4dabf5;
        }
        .calculator {
            background-color: #132f4c;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #81c784;
        }
        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #2c5282;
            border-radius: 4px;
            background-color: #1a3b5d;
            color: #e0e0e0;
        }
        button {
            background-color: #4caf50;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 10px;
            font-weight: bold;
        }
        button:hover {
            background-color: #388e3c;
        }
        .results {
            margin-top: 20px;
            padding: 15px;
            background-color: #1e3a5f;
            border-radius: 6px;
            display: none;
        }
        .highlight {
            font-weight: bold;
            color: #ff9800;
        }
        .explanation {
            background-color: #1e3a5f;
            padding: 15px;
            border-radius: 6px;
            margin-top: 20px;
        }
        .formula {
            font-family: monospace;
            background-color: #0d2240;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
            margin: 10px 0;
        }
        .note {
            background-color: #263238;
            padding: 10px;
            border-left: 4px solid #ff9800;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <h1>Sci-Fi Spacetime Dilation Calculator</h1>
    <p>Calculate how much time passes on Earth while your characters travel to distant star systems.</p>
    
    <div class="calculator">
        <div class="form-group">
            <label for="destination">Destination:</label>
            <select id="destination">
                <option value="custom">Custom Distance</option>
                <option value="proxima_centauri" selected>Proxima Centauri (4.24 light-years)</option>
                <option value="barnards_star">Barnard's Star (5.96 light-years)</option>
                <option value="sirius">Sirius (8.6 light-years)</option>
                <option value="tau_ceti">Tau Ceti (11.9 light-years)</option>
                <option value="gliese_667C">Gliese 667C (22 light-years)</option>
                <option value="vega">Vega (25 light-years)</option>
                <option value="trappist">TRAPPIST-1 (39 light-years)</option>
                <option value="kepler_442b">Kepler-442b (1,200 light-years)</option>
                <option value="andromeda">Andromeda Galaxy (2.5 million light-years)</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="distance">Distance (light-years):</label>
            <input type="number" id="distance" value="4.24" min="0.1" step="0.01">
        </div>
        
        <div class="form-group">
            <label for="warpFactor">Warp Factor (1.0 = speed of light):</label>
            <input type="number" id="warpFactor" value="2" min="0.1" step="0.1">
        </div>

        <div class="form-group">
            <label for="shipTime">Journey Duration for the Crew (years):</label>
            <input type="number" id="shipTime" value="1" min="0.1" step="0.1">
        </div>
        
        <button onclick="calculateTimeDilation()">Calculate</button>
        
        <div id="results" class="results">
            <h3>Results:</h3>
            <p>Distance: <span id="resultDistance" class="highlight"></span> light-years</p>
            <p>Warp Factor: <span id="resultWarp" class="highlight"></span> (speed of light = 1.0)</p>
            <p>Actual Velocity: <span id="resultVelocity" class="highlight"></span> × speed of light</p>
            <p>Journey Duration for Crew: <span id="resultShipTime" class="highlight"></span> years</p>
            <p>Time Passed on Earth: <span id="resultEarthTime" class="highlight"></span> years</p>
            <p>Time Dilation Factor: <span id="resultDilationFactor" class="highlight"></span></p>
        </div>
    </div>
    
    <div class="explanation">
        <h2>How to Use This in Your Screenplay</h2>
        <p>Time dilation is a powerful storytelling device. Here are some ways to use these calculations:</p>
        <ul>
            <li><strong>Emotional impact:</strong> A character returns from a journey to find their loved ones have aged significantly or passed away.</li>
            <li><strong>Plot device:</strong> Information or technology becomes outdated during transit.</li>
            <li><strong>Character development:</strong> Different experiences of time can create interesting character dynamics.</li>
        </ul>
        
        <h3>Warp Speed Models</h3>
        <p>This calculator uses two models depending on the warp factor:</p>
        
        <h4>Sublight Speed (Warp < 1.0)</h4>
        <p>For speeds less than light speed, we use Einstein's special relativity time dilation:</p>
        <div class="formula">Earth Time = Ship Time / √(1 - v²/c²)</div>
        <p>This creates the "twin paradox" effect where time passes more slowly for the travelers.</p>
        
        <h4>FTL - Faster Than Light (Warp > 1.0)</h4>
        <p>For warp speeds, we use a fictional model based on Star Trek's warp field theory:</p>
        <div class="formula">
            Effective Velocity = Warp³ × c (for Warp ≤ 5)<br>
            Effective Velocity = Warp⁵ × c (for 5 < Warp ≤ 10)
        </div>
        <p>This creates exponentially increasing speeds, while time dilation effects are calculated based on the ship's relativistic frame.</p>
        
        <div class="note">
            <strong>Note for screenwriters:</strong> While scientifically implausible, FTL travel makes for better storytelling. This calculator provides a consistent framework for your story. Feel free to adjust the details to suit your narrative needs!
        </div>
    </div>

    <script>
        // Pre-defined star systems and their distances
        const starSystems = {
            proxima_centauri: 4.24,
            barnards_star: 5.96,
            sirius: 8.6,
            tau_ceti: 11.9,
            gliese_667C: 22,
            vega: 25,
            trappist: 39,
            kepler_442b: 1200,
            andromeda: 2500000
        };

        // Update distance when destination changes
        document.getElementById('destination').addEventListener('change', function() {
            const selectedSystem = this.value;
            if (selectedSystem !== 'custom') {
                document.getElementById('distance').value = starSystems[selectedSystem];
            }
        });

        function calculateTimeDilation() {
            // Get input values
            const distance = parseFloat(document.getElementById('distance').value);
            const warpFactor = parseFloat(document.getElementById('warpFactor').value);
            const shipTime = parseFloat(document.getElementById('shipTime').value);
            
            // Calculate actual velocity as a factor of c
            let velocity;
            if (warpFactor <= 5) {
                velocity = Math.pow(warpFactor, 3);
            } else {
                velocity = Math.pow(warpFactor, 5);
            }
            
            // Calculate Earth time
            let earthTime;
            let dilationFactor;
            
            if (warpFactor < 1) {
                // Sublight relativistic time dilation
                const gamma = 1 / Math.sqrt(1 - Math.pow(warpFactor, 2));
                earthTime = shipTime * gamma;
                dilationFactor = gamma;
            } else {
                // FTL travel - use fictional warp model
                // Basic transit time at warp speed
                const transitTime = distance / velocity;
                
                // Apply a fictional dilation factor for FTL travel
                // This makes higher warp factors have less dilation effect
                // to create more dramatically useful results
                const warpDilation = 0.5 + (0.5 / warpFactor);
                earthTime = transitTime / warpDilation;
                dilationFactor = warpDilation;
                
                // Ensure ship time is consistent with our model
                if (Math.abs(transitTime - shipTime) > 0.01) {
                    // If ship time differs from calculated transit time, 
                    // recalculate earth time based on provided ship time
                    earthTime = shipTime / warpDilation;
                }
            }
            
            // Display results
            document.getElementById('resultDistance').textContent = distance.toFixed(2);
            document.getElementById('resultWarp').textContent = warpFactor.toFixed(2);
            document.getElementById('resultVelocity').textContent = velocity.toFixed(2);
            document.getElementById('resultShipTime').textContent = shipTime.toFixed(2);
            document.getElementById('resultEarthTime').textContent = earthTime.toFixed(2);
            document.getElementById('resultDilationFactor').textContent = dilationFactor.toFixed(4);
            
            // Show results
            document.getElementById('results').style.display = 'block';
        }
    </script>
</body>
</html>
```

## How to Use This Calculator

1. Save this entire Markdown file as an HTML file (change the extension to .html)
2. Open the HTML file in any web browser
3. Input your destination, warp factor, and journey duration
4. Click "Calculate" to see how much time passes on Earth during the journey

## Narrative Considerations

When incorporating time dilation into your screenplay, consider:

1. **The "Return Home" Problem**: Characters returning to Earth after a journey may find everything changed
2. **Communication Delays**: Messages sent between Earth and the ship will be received at different points in subjective time
3. **Technological Evolution**: Earth technology might advance significantly during long journeys
4. **Cultural Shifts**: Society on Earth could transform dramatically while travelers experience only a short subjective time

This calculator balances scientific accuracy (for sublight speeds) with dramatic storytelling potential (for FTL travel), giving you consistent numbers to work with in your science fiction narrative.
