SELECT * FROM ventes;
SELECT SUM(prix * qte) FROM ventes ;
SELECT produit, SUM(qte), SUM(prix * qte) FROM ventes GROUP BY produit;
SELECT region, SUM(qte), SUM(prix * qte) FROM ventes GROUP BY region;