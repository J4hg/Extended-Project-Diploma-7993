from astropy import units as u
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
from astropy.time import Time # imports all the  necessary data from the poliastro and astropy libraries

semimajor_axis = 0.00257188 * u.AU # half the longest diameter of an ellipse, runs from the center of the ellipse to the furthest edge along the axis
eccentricity = 0.0549 * u.one # measure of how much an orbit deviates from being a perfect circle
inclination = 5.15 * u.deg # tilt of an orbits plane relative to a reference plane
right_ascension_of_ascending_node = 125.08 * u.deg # the angle that locates where an orbit crosses the reference plane
argument_of_periapsis = 318.15 * u.deg # the angle within the orbital plane from the ascending node to the pericenter
true_anomaly = 0.0 * u.deg # the angle between the pericenter direction and the current position of the orbiting body

epoch = Time("2025-11-30 17:15", scale="utc") # sets the initial point in time to the current time/date

moon_orbit = Orbit.from_classical(Earth, semimajor_axis, eccentricity, inclination, right_ascension_of_ascending_node, argument_of_periapsis, true_anomaly, epoch = epoch) # this defines the orbit using the element data I set, my data corresponds to the moon orbit around the earth


seconds = 0
for x in range(1,84000): # for loop that increments through a full day in seconds
    seconds += 1
    moon_orbit_s = moon_orbit.propagate(seconds * u.second) # propagates the orbit once per second
    print (moon_orbit_s.nu.to(u.deg), moon_orbit_s.epoch) # prints the true anomaly angle and the epoch

