# ⛵️ Celestial Navigation Scripts 🌍✨

A collection of Python scripts to assist with celestial navigation, providing tools for sight reductions, altitude corrections, and position calculations. These scripts support navigators in determining their position at sea using astronomical observations, such as sextant sights of the sun, moon, planets, and stars. 

### Key Features:
- 🌞 **Noon Sight Calculations**: Determine latitude using solar altitude at noon.
- 🌌 **Sight Reduction**: Convert sextant readings into usable coordinates.
- 📐 **Altitude Corrections**: Apply corrections for index error, refraction, parallax, and dip.
- ⏱️ **Time and Longitude Calculations**: Convert local observations to universal time.

Ideal for sailors, navigators, and students of celestial navigation.

### Unite Tests
To run the tests execute:
```bash 
python -m unittest discover tests
```

### Examples
#### Observation Time
```bash
echo -e "174°30'E\n2024-06-22T02:00:00\n2024-06-22T03:06:00\n2024-06-22T03:51:00" | python main.py observationtime
```

## Author
- Kevin Veen-Birkenbach  
- 🌐 [Website](https://www.yachtmaster.world)  
- 📧 kevin@veen.world

---
This repository was created with the help of [AI](https://chatgpt.com/c/67138609-6ab8-800f-a091-a42e04bf3c9f). 
