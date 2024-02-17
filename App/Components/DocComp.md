## Parts

El Wizard Wizard esta compost de una llista d'element per el quals pots fer scroll.
S'haurien d'afegir a scrollable_frame, cada un dels tipus d'entrada en el fitxer del main equival a un tipus diferent 
segons la paraula utilitzada com a identificador:

- **Bool** \
Utilitza el _CompBool_ i mostra el nom del parametre i un boto radial per marcar el valor.
- **Int-Range** \
Utilitza el _CompIntRange_ i mostra el nom del parametre i un slider per marcar el valor dins dels dos numeros definits en el fitxer constructor del wizard.
Es mostra tambe el valor actual a la part esquerra.
- **Set** \
Utilitza el *CompSet*, permet seleccionar entre un conjunt de elements definit en l'inici amb un drop down menu.
