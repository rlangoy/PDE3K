PD-PDE3000-1 20V Produktdesign 2
================================

Dette er materiale som brukes i undervisningen i faget PD-PDE3000-1 ved USN 

`USN Produktdesign <https://www.usn.no/studier/finn-studier/teknologi-ingeniorfag-og-lysdesign/produktdesign/>`_


Python Function Example1
------------------------

.. code-block:: python

  def beregnAreal(radius):
        "Beregner arealet til en sirkel"
        return radius*radius*3.14 



Python Function Example2
------------------------
.. code-block:: python

  import math # Importerer matte biblioteket
  class SIRKEL():
      """Klasse beregning av et sirkulært areal
      param: radius: sirkelsens radius
      :type  radius: float
      """    

      def __init__(self,radius):
          self.radius=radius

      radius=0.0
      """ Sirkelens radius
      :type radius: float 
      """

      def getAreal(self):
          "Beregner arealet til en sirkel"
          return self.radius*self.radius*math.pi


Micropython øvelser
===================

Her er Micropython øvelsene `Thonny IDE tutorial`_.

.. _Thonny IDE tutorial: https://github.com/rlangoy/PDE3K/blob/master/docs/thonny_guide.rst
