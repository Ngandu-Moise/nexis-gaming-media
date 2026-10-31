# Playbook — publication quotidienne Nexis Gaming

Ce fichier est la consigne que suit la tâche programmée chaque jour. Il peut être modifié
à tout moment par Nexis Gaming ; la tâche relit toujours la dernière version.

## Contexte

- Boutique : Nexis Gaming, consoles, jeux, installation et réparation.
- Adresse : avenue du 30 Juin, face à Netflix, près du rond-point Malu, Kolwezi (RDC).
- Comptes : TikTok @nexisgs, Instagram @nexisgaming13, chaîne YouTube, via Metricool.
- Marque Metricool : brandId `2916492` (libellé « Boa Games »). Ne jamais publier sur Facebook.
- Fuseau du public : Africa/Lubumbashi (UTC+2). Lire le fuseau de la marque avec
  getBrandSettings à chaque exécution et convertir l'heure de publication en conséquence.

## Règles de contenu

- Vidéo verticale 1080x1920, 18 à 28 secondes, voix off française sur chaque écran.
- Écran 1 = accroche en moins de 2 s (question, chiffre, « attention », compte à rebours).
- 2 ou 3 écrans de contenu, puis l'écran de fin (adresse + @nexisgs, ajouté automatiquement).
- Ton : jeune, direct, tutoiement, français simple. Pas de vulgarité, pas de politique.
- Prix et disponibilités : UNIQUEMENT ceux de `produits.md`. Liste vide ou produit absent
  = ne citer aucun prix ni stock. Ne jamais inventer de promotion, de prix ou de date.
- Actualité gaming : seulement des faits vérifiés par une recherche web le jour même.
- Pas de personnage, logo ou image protégés (pas de visuel GTA, PlayStation, etc.) :
  le texte peut nommer les jeux et consoles, l'image reste la charte Nexis.
- Ne pas répéter un sujet publié dans les 10 derniers jours (voir `journal.md`).

## Calendrier

Jusqu'au 19 novembre 2026 : un sujet GTA 6 par jour (compte à rebours J-x, quelle console,
config, conseils pour bien démarrer, rappel « pas sur PS4 »). Le 19 novembre : « GTA 6 est
sorti aujourd'hui », appel à venir jouer ou s'équiper en boutique.

Ensuite, thème par jour :

| Jour | Heure (Kolwezi) | Thème |
| --- | --- | --- |
| Lundi | 18 h | Stock et prix (produits.md ; sinon services de la boutique) |
| Mardi | 18 h | Réparation : un problème courant et ses signes (manette qui dérive, surchauffe, HDMI) |
| Mercredi | 18 h | Actualité gaming vérifiée |
| Jeudi | 18 h | Conseil d'achat ou comparatif (sans prix si absent de produits.md) |
| Vendredi | 18 h | Humour gaming : situation que tout joueur connaît |
| Samedi | 12 h | Défi ou quiz gaming (« commente ta réponse ») |
| Dimanche | 12 h | Astuce de jeu ou d'entretien de console |

## Procédure quotidienne

1. `bash tools/setup.sh`
2. Lire `journal.md`, `produits.md` et ce playbook.
3. Choisir le sujet du jour selon le calendrier ; vérifier par recherche web toute info d'actualité.
4. Écrire `specs/AAAA-MM-JJ.json` (scenes : kicker, title, body, voice, accent_last ; cta true).
5. `python3 tools/render.py specs/AAAA-MM-JJ.json videos/AAAA-MM-JJ.mp4`
   puis regarder 2 images clés (texte lisible, rien de coupé). Durée cible 18–28 s.
6. `git add` + commit + `git push` ; vérifier que
   `https://raw.githubusercontent.com/Ngandu-Moise/nexis-gaming-media/main/videos/AAAA-MM-JJ.mp4`
   répond (HTTP 200).
7. createScheduledPost (Metricool) le jour même à l'heure du calendrier, convertie dans le fuseau
   de la marque :
   - providers : tiktok, instagram, youtube ; autoPublish true ; media = l'URL ci-dessus
   - instagramData : {"type": "REEL", "showReelOnFeed": true}
   - youtubeData : {"title": "<titre court + #Shorts>", "type": "short", "privacy": "public",
     "madeForKids": false, "category": "GAMING"}
   - tiktokData : {"privacyOption": "PUBLIC_TO_EVERYONE", "title": "<accroche>"}
   - texte : accroche + 1 phrase + appel à l'action (DM, adresse) + 3 à 5 hashtags
     (1 local : #kolwezi/#rdcongo, 1 produit, 1 communauté : #gamingrdc)
   - firstCommentText : une question pour lancer les commentaires
   Si l'heure est déjà passée, publier 30 minutes plus tard.
8. Ajouter une ligne à `journal.md` (date, sujet, durée, URL Metricool), commit + push.
9. Dimanche : lire les stats Metricool de la semaine (vues, partages, abonnés par vidéo TikTok),
   ajouter un bilan de 5 lignes dans `journal.md` et adapter les sujets de la semaine suivante.
10. En cas d'échec (Metricool refuse, rendu impossible) : écrire l'erreur dans `journal.md`
    et la signaler dans le message de fin.
