from astropy import units as u
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
from poliastro.plotting.static import StaticOrbitPlotter
from astropy.time import Time # imports all the  necessary data from the poliastro and astropy libraries
from poliastro.frames import Planes


semimajor_axis = 384440 * u.km # half the longest diameter of an ellipse, runs from the center of the ellipse to the furthest edge along the axis
eccentricity = 0.0549 * u.one # measure of how much an orbit deviates from being a perfect circle
inclination = 0.0 * u.deg # tilt of an orbits plane relative to a reference plane
right_ascension_of_ascending_node = 0.0 * u.deg # the angle that locates where an orbit crosses the reference plane
argument_of_periapsis = 0.0 * u.deg # the angle within the orbital plane from the ascending node to the pericenter
true_anomaly = 0.0 * u.deg # the angle between the pericenter direction and the current position of the orbiting body

epoch = Time("2025-12-5 12:00", scale="utc") # sets the initial point in time to the current time/date

moon_orbit = Orbit.from_classical(Earth, semimajor_axis, eccentricity, inclination, right_ascension_of_ascending_node, argument_of_periapsis, true_anomaly, epoch = epoch, plane=Planes.EARTH_ECLIPTIC) # this defines the orbit using the element data I set, my data corresponds to the moon orbit around the earth


Orb = StaticOrbitPlotter()
Orb.plot(moon_orbit, label="Moon Orbit")
import matplotlib.pyplot as plt

plt.show()

