# Playbook — publication Nexis Gaming

Ce fichier est la consigne que suit la tâche programmée chaque jour. Il peut être modifié
à tout moment par Nexis Gaming ; la tâche relit toujours la dernière version.
Plan détaillé et calculs : https://claude.ai/artifact/MSnUWa3NpyenDBpPeLwz1t

## Contexte

- Boutique : Nexis Gaming, consoles, jeux, installation et réparation.
- Adresse : avenue du 30 Juin, face à Netflix, près du rond-point Malu, Kolwezi (RDC).
- Comptes : TikTok @nexisgs, Instagram @nexisgaming13, chaîne YouTube, via Metricool.
- Marque Metricool : brandId `2916492` (libellé « Boa Games »). Ne jamais publier sur Facebook.
- Fuseau du public : Africa/Lubumbashi (UTC+2). Lire le fuseau de la marque avec
  getBrandSettings à chaque exécution et convertir l'heure de publication en conséquence.
- Higgsfield : abonnement Pro à partir du 3 novembre 2026, 600 crédits par cycle d'un mois,
  renouvelés le 3 de chaque mois (cycle du 3 au 2 du mois suivant).
  Le propriétaire a donné une autonomie totale pour les sujets et la production.

## Rythme (à partir du 3 novembre 2026)

- **Une vidéo de haute qualité tous les 2 jours** : jours de publication = 3, 5, 7… novembre,
  en comptant sans interruption d'un mois à l'autre (29 nov. → 1er déc. → 3 déc. … 31 déc. → 2 janv.).
  Test : `python3 -c "import datetime as d;print((d.date.today()-d.date(2026,11,3)).days%2==0)"` → True = jour de publication.
- Heure : 18 h en semaine, 12 h le samedi et le dimanche (heure de Kolwezi).
- Le 2 novembre 2026 seulement : vidéo motion design sans clip IA (abonnement pas encore actif),
  avec la voix ElevenLabs (≈ 2 crédits sur le solde gratuit restant).
- Jour sans publication : ne rien créer. Vérifier seulement que la publication de la veille est
  bien partie (getScheduledPosts) et le solde Higgsfield (balance). Signaler un problème, sinon rien.

## Sujets : les formats les plus populaires du gaming

Choisir chaque fois le sujet le plus fort du moment dans le pilier du jour. Chaque dimanche (bilan), on se demande
« qu'est-ce que les joueurs regardent cette semaine ? » : jeux les plus joués et les plus vendus,
sorties, actu, tendances TikTok gaming (recherche web), plus nos meilleures vidéos (Metricool).

| Jour | Pilier | Exemples |
| --- | --- | --- |
| Lundi | Déballage (console, manette, accessoire) | « On ouvre la manette sans fil », « ce qu'il y a dans la boîte » |
| Mardi | Réparation et entretien | manette qui dérive, surchauffe, port HDMI, nettoyage |
| Mercredi | Jeux phares : actu vérifiée | GTA 6, EA Sports FC, Call of Duty, Fortnite : sortie, mise à jour, nouveauté |
| Jeudi | Déballage ou comparatif | PS5 ou Xbox Series ? quelle manette choisir ? |
| Vendredi | Humour gaming | coupure de courant pendant le match, manette à 1 % de batterie, le pote qui met pause |
| Samedi | Défi ou quiz | « devine le jeu », « commente ton score » |
| Dimanche | Astuces de jeu | réglages, astuces pour bien démarrer un jeu phare, gestion du stockage |

- Jusqu'au 19 novembre 2026, les sujets « jeux phares » parlent en priorité de GTA 6 (sortie le
  19 novembre sur PS5 et Xbox Series X|S). Le 19 novembre : « GTA 6 est sorti aujourd'hui ».
- Si les statistiques montrent qu'un pilier marche nettement mieux, il peut remplacer
  un autre jour pendant une semaine (le noter dans le bilan).
- « Extraits de jeux phares » : jamais d'images réelles d'un jeu (droits d'auteur) ni de recréation
  IA d'un jeu, d'un personnage ou d'un lieu protégé. On montre des joueurs fictifs qui réagissent,
  l'écran ne montre que de la lumière colorée ; le texte et la voix nomment le jeu.
- Déballage : la vidéo IA montre une console ou une manette générique sans logo. Ne jamais dire
  que le produit est en stock ou citer un prix s'il n'est pas dans `produits.md`.
- Dossier `rushes/` : si Nexis Gaming y dépose de vraies vidéos (déballage, atelier, boutique),
  les utiliser en priorité comme clips (champ "clip" : "rushes/fichier.mp4"), sans crédit.

## Règles de contenu

- Vidéo verticale 1080x1920, 22 à 28 secondes, voix off française sur chaque scène.
- Scène 1 = accroche en moins de 2 s (question, chiffre, « attention », réaction forte).
- Ton : jeune, direct, tutoiement, français simple. Pas de vulgarité, pas de politique.
- Prix et disponibilités : UNIQUEMENT ceux de `produits.md`. Liste vide ou produit absent
  = ne citer aucun prix ni stock. Ne jamais inventer de promotion, de prix ou de date.
- Actualité : seulement des faits vérifiés par une recherche web le jour même.
- Aucun logo, personnage, jeu ou visuel protégé (GTA, PlayStation, Xbox, FC…) dans les images ;
  personnes fictives uniquement, aucune ressemblance avec une vraie personne.
- Ne pas répéter un sujet publié dans les 10 derniers jours (voir `journal.md`).

## Format d'une vidéo (moteur « motion »)

| Scène | Durée | Contenu | Source | Crédits |
| --- | --- | --- | --- | --- |
| 1 Accroche | ~5 s | clip IA + titre | Kling 3.0 | 8,75 |
| 2 Contenu | ~5 s | clip IA + texte | Kling 3.0 | 8,75 |
| 3 Contenu | ~5 s | clip IA + texte | Kling 3.0 | 8,75 |
| 4 Info clé | 4–6 s | liste, gros chiffre, comparatif sur fond animé | motion | 0 |
| Fin | ~5 s | NEXIS GAMING + adresse (automatique) | motion | 0 |
| Voix off | toute la vidéo | voix naturelle ElevenLabs, une piste par scène + fin | Higgsfield | ≈ 2 |

Spec `specs/AAAA-MM-JJ.json` (voir l'en-tête de `tools/motion/make_video.py`) :
`{"engine": "motion", "scenes": [{"kicker", "title" ("\n" = nouvelle ligne), "accent_last", "body",
"big", "items", "cross", "voice", "voice_url", "clip"}], "cta": true, "cta_voice", "cta_voice_url"}`.
Voix : 1 ou 2 phrases courtes par scène ; "voice" garde le texte, "voice_url" l'audio ElevenLabs.

### Voix off naturelle (ElevenLabs via Higgsfield)

- generate_audio_batch, une requête par scène + une pour la fin : model `text2speech_v2`,
  variant `elevenlabs`, voice_type `preset`, voice_id = VOIX ci-dessous, prompt = texte de la scène,
  use_unlim false. Puis jobs_wait ; chaque result_url va dans "voice_url" (fin : "cta_voice_url").
  Coût ≈ 0,45 crédit pour 130 caractères, soit ≈ 2 crédits par vidéo.
- VOIX : `f1e8226e-2248-4d5f-b43c-0a79e9949dbf` (voix masculine « Andre »).
  Voix féminine possible : `023ebf5e-1970-40d8-825c-a5ef6a1dd4ff` (« Ines »). Garder la même voix
  partout, c'est la voix de la marque.
- Écrire les nombres, sigles et noms tels qu'ils se prononcent si besoin (« Xbox Série X et S »,
  « PS5 »). Ponctuation expressive (« ! », « ? ») : la voix suit l'intonation.
- Si Higgsfield ne répond pas : laisser seulement "voice" (Piper, hors ligne) et le noter.

### Clips Higgsfield

- generate_video_batch, 3 requêtes : model `kling3_0`, aspect_ratio `9:16`, duration 5,
  mode `pro`, sound `off`, use_unlim false. Avant : generate_video avec get_cost true pour
  vérifier le prix (8,75 attendu) et balance pour le solde. Puis jobs_wait jusqu'à la fin.
- Style commun des prompts (en anglais) : vertical cinematic shot, night, small modern video game
  shop or gamer bedroom lit by cyan and magenta neon, young Black African people in casual
  streetwear (fictional), plain black consoles/controllers with no logos, screens showing only
  abstract colorful light, realistic, shallow depth of field, slow camera move.
  Toujours ajouter : « No text, no logos, no brand names, no recognizable game footage. »
- L'URL du résultat de chaque clip va dans le champ "clip" de sa scène.

### Montage

- Commit + push du spec : le workflow GitHub « Rendu vidéo » télécharge les clips, monte la vidéo
  (≈ 6 à 10 min) et pousse `videos/AAAA-MM-JJ.mp4`. Attendre avec
  `gh api repos/Ngandu-Moise/nexis-gaming-media/contents/videos/AAAA-MM-JJ.mp4` (toutes les 30 s,
  20 min maximum), puis `git pull`. Échec : lire le journal du run (outils GitHub Actions).
- Contrôle : extraire une image au milieu de chaque scène (ffmpeg) et les regarder. Refuser :
  mains ou visages déformés, logo ou texte parasite, élément protégé, texte illisible ou coupé.
- Clip refusé : le refaire une seule fois (nouveau prompt), repousser le spec. Second échec :
  retirer le "clip" de cette scène (fond animé). La vidéo sort quand même.
- Sans abonnement ou en cas de panne Higgsfield : vidéo sans clip (0 crédit), le noter.

## Budget de crédits (600 par cycle, du 3 au 2 du mois suivant)

- Coût de base d'une vidéo : 3 clips (26,25) + voix (≈ 2) = **≈ 28,25 crédits**.
  Cycle de 15 vidéos : ≈ 424 crédits ; il reste ≈ 176 crédits pour les reprises et la fin de cycle.
- Les crédits non utilisés ne sont pas reportés : ils sont dépensés sur les **3 dernières vidéos
  du cycle** (pour le premier cycle : 27 nov., 29 nov. et 1er déc.).
- Avant de générer, compter V = vidéos restantes jusqu'au 2 inclus (jours de publication restants).
  - V > 3 : besoin = V × 28,25. Solde ≥ besoin → 3 clips. Solde < besoin → 2 clips.
    Solde < 10 → aucun clip (voix seule si possible).
  - V ≤ 3 (fin de cycle) : budget de la vidéo = (solde − 9) / V, où 9 crédits restent pour
    une reprise. Avec ce budget, ajouter dans l'ordre : 4e clip, 5e clip (vidéo entièrement IA),
    puis clip d'accroche en 10 s (17,5 au lieu de 8,75). Pour la toute dernière vidéo (V = 1),
    budget = solde, une fois la reprise éventuelle faite.
- Solde < 100 crédits avant le 20 du cycle → notification au propriétaire.
- Ne jamais acheter de crédits ni changer d'abonnement.

## Publication Metricool

createScheduledPost le jour même à l'heure prévue, convertie dans le fuseau de la marque :
- providers : tiktok, instagram, youtube ; autoPublish true ;
  media = `https://raw.githubusercontent.com/Ngandu-Moise/nexis-gaming-media/main/videos/AAAA-MM-JJ.mp4`
- instagramData : {"type": "REEL", "showReelOnFeed": true, "isAiGenerated": true si clips IA}
- youtubeData : {"title": "<titre court + #Shorts>", "type": "short", "privacy": "public",
  "madeForKids": false, "category": "GAMING", "isAiGeneratedContent": true si clips IA}
- tiktokData : {"privacyOption": "PUBLIC_TO_EVERYONE", "title": "<accroche>", "isAigc": true si clips IA}
- texte : accroche + 1 phrase + appel à l'action (DM, adresse) + 3 à 5 hashtags
  (1 local : #kolwezi/#rdcongo, 1 jeu ou produit, 1 communauté : #gamingrdc)
- firstCommentText : une question pour lancer les commentaires
- Si l'heure est déjà passée, publier 30 minutes plus tard.

## Journal et bilan

- `journal.md` : date, sujet, durée, clips (générés / refaits), voix, crédits dépensés, solde, id Metricool.
- Dimanche : bilan de la semaine (vues, partages, abonnés par vidéo TikTok via Metricool ;
  crédits dépensés et solde), puis choix des sujets de la semaine suivante selon les tendances.
- En cas d'échec : écrire l'erreur dans `journal.md` et notifier le propriétaire.
