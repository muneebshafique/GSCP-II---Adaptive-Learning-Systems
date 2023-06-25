

class KnowledgeBase:
    def __init__(self) -> None:
        self.syllabus= {
            'Motion, forces and energy':{
                'Physical quantities and measurement techniques': [],
                'Motion': [],
                'Mass and Weight': [],
                'Density': [],
                'Forces': ['Balanced and unbalanced forces', 'Friction', 'Elastic deformation', 'Circular motion','Turning effect of forces','Centre of gravity'],
                'Momentum':[],
                'Energy, work and power ': ['Energy', 'Work', 'Energy resources', 'Efficiency','Power'],
                'Pressure':[]
                },
            'Thermal physics':{
                'Kinetic particle model of matter': ['States of matter', 'Particle model'],
                'Thermal properties and temperatuare': ['Thermal expansion of solids, liquids and gases', 'Specific heat capacity','Melting, boiling and evaporation'],
                'Transfer of thermal energy': ['Conduction', 'Convection', 'Radiation', 'Consequences of thermal energy transfer']
                },
            'Waves':{
                'General properties of waves':[],
                'Light': ['Reflection of light', 'Refraction of light','Thin lenses', 'Dispersion of light'],
                'Electromagnetic spectrum':[],
                'Sound':[]
                },
            'Electricity and magnetism':{
                'Simple magnetism and magnetic field': [],
                'Electrical quantities':['Electrical charge', 'Electrical current', 'Electromotive force and potential difference', 'Resistance'],
                'Electric Circuits':['Circuit diagram and circuit components', 'Series and parallel circuits','Action and use of circuit components'],
                'Practical Electricity':['Uses of electricity','Electrical Safety'],
                'Electromagnetic effects ':['Electromagnetic induction', 'The a.c. generator', 'Magnetic effect of a current','Forces on a current-carrying conductor', 'The d.c. motor', 'The transformer'],
                'Uses of Oscilloscope':[],
            },
            'Nuclear physics':{
                'The nuclear model of the atom':['The atom','The nucleus'],
                'Radioactivity':['Detection of radioactivity', 'The three types of emission', 'Radioactive decay','Fission and fusion','Half-life','Safety precautions']
            },
            'Space physics':{
                'Earth and the Solar System':['The earth','The solar system'],
                'Stars and the Universe':['The sun as a star', 'Stars', 'The universe']
            }
        }


    def stats_from_syllabus(self):
        pass