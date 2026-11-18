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
- Heure (heure de Kolwezi) : **18 h du lundi au vendredi**, **10 h le samedi et le dimanche**,
  **10 h le jour d'un grand événement** (ex. sortie de GTA 6 le 19 nov.). Source : meilleur moment
  Metricool TikTok (pics à 10 h et 18 h) ; à réévaluer au bilan du dimanche avec nos propres vues.
- **Vidéo de vidage** : le dernier jour du cycle (le 2 du mois), s'il reste ≥ 28,25 crédits après
  la dernière vidéo, publier une vidéo bonus à 18 h (10 h le week-end) pour ne perdre aucun crédit
  (voir « Budget »). Si le 2 est déjà un jour de publication, c'est lui la dernière vidéo et elle
  prend tout le reste.
- Jour sans publication (sauf vidéo de vidage du 2) : ne rien créer. Vérifier seulement que la publication de la veille est
  bien partie (getScheduledPosts) et le solde Higgsfield (balance). Signaler un problème, sinon rien.

## Sujets : les formats les plus populaires du gaming

Choisir chaque fois le sujet le plus fort du moment dans le pilier du jour. Chaque dimanche (bilan), on se demande
« qu'est-ce que les joueurs regardent cette semaine ? » : jeux les plus joués et les plus vendus,
sorties, actu, tendances TikTok gaming (recherche web), plus nos meilleures vidéos (Metricool).

| Jour | Pilier | Exemples |
| --- | --- | --- |
| Lundi | Histoire d'un jeu légendaire | la saga GTA de 1997 à GTA 6, FIFA devenu EA Sports FC, Mario, Call of Duty, Mortal Kombat : dates clés, chiffres de ventes vérifiés |
| Mardi | Réparation PlayStation et manette | manette qui dérive, PS5 qui surchauffe, port HDMI, bouton qui ne répond plus, nettoyage |
| Mercredi | Jeux phares : actu vérifiée et classements | GTA 6, EA Sports FC, Call of Duty ; « top 5 des meilleurs jeux de l'année » (notes Metacritic/OpenCritic, nommés et lauréats des Game Awards, vérifiés le jour même) |
| Jeudi | Consoles : puissance et comparatifs (ou déballage) | « les consoles les plus puissantes » (téraflops, résolution, fps : fiches techniques officielles), PS5 Pro ou Xbox Series X ? quelle manette choisir ? |
| Vendredi | Humour gaming | coupure de courant pendant le match, manette à 1 % de batterie, le pote qui met pause |
| Samedi | Quiz ou défi | « devine le jeu », « devine la console à son bruit », vrai ou faux gaming |
| Dimanche | Astuces de jeu | réglages, astuces pour bien démarrer un jeu phare, gestion du stockage |

- Jusqu'au 19 novembre 2026, les sujets « jeux phares » parlent en priorité de GTA 6 (sortie le
  19 novembre sur PS5 et Xbox Series X|S), sauf le 11 nov. (Top 5 des jeux de 2026, décision du
  propriétaire le 10 nov. pour éviter trop de GTA d'affilée). Le 19 novembre : « GTA 6 est sorti aujourd'hui ».
- Si les statistiques montrent qu'un pilier marche nettement mieux, il peut remplacer
  un autre jour pendant une semaine (le noter dans le bilan).
- Noms : les jeux, consoles et marques (GTA 6, PS5, Xbox, EA Sports FC…) sont nommés librement
  dans les titres, la voix, la légende et les hashtags (demande du propriétaire, 7 nov. 2026).
- Images de produits réels (pochettes, boîtes, consoles et manettes officielles avec leur logo) :
  uniquement via les vidéos et photos filmées par Nexis Gaming dans `rushes/` (produits de la
  boutique). Les clips IA, eux, ne recréent jamais un logo, une pochette, une affiche, un personnage
  ou un jeu : joueurs fictifs, consoles noires génériques, écrans en lumière colorée.
- Classements et comparatifs : chaque rang, note ou chiffre technique vient d'une source vérifiée
  le jour même (citée dans `journal.md`). Le titre du jeu ou le chiffre s'affiche en gros texte animé.
- Déballage : sans rush, la vidéo IA montre une console ou une manette générique sans logo. Ne jamais
  dire que le produit est en stock ou citer un prix s'il n'est pas dans `produits.md`.
- Dossier `rushes/` : si Nexis Gaming y dépose de vraies vidéos (déballage, atelier, boutique),
  les utiliser en priorité comme clips (champ "clip" : "rushes/fichier.mp4"), sans crédit.

## Ce qui marche dans le gaming court (étude du 7 nov. 2026)

Sources : classements Buzzlytics, Heepsy et Hooked (comptes TikTok gaming les plus suivis et les plus vus),
guides Socialync, Viryze et FluxNote (algorithme Shorts/TikTok 2026). Les plus gros comptes (Ibai, Ninja,
Fortnite, Roblox, Subway Surfers) misent sur trois formats : « accroche + démonstration » (tuto, produit
montré), sketch d'humour court, compilation de moments forts. Ce qu'on en applique :

- **Accroche en 1,5 s** : une question ou une contradiction (« Ta PS5 chauffe ? Ce n'est pas la poussière. »),
  un chiffre choc ou un classement (« Le n°1 va te surprendre »). Éviter les accroches « POV ». La 1re ligne
  de la légende reprend l'accroche.
- **Rythme** : jamais plus de 4 à 5 s sur le même plan ; une idée par scène ; pas d'introduction, pas de contexte inutile.
- **Texte à l'écran** : chaque phrase dite apparaît en gros texte (la majorité regarde sans le son).
- **Boucle** : la dernière phrase avant la fin renvoie à l'accroche (« Alors, t'avais trouvé ? »), pour
  donner envie de revoir la vidéo.
- **Durée** : 25 à 35 s. En dessous de 15 s, les Shorts sont moins poussés.
- **Séries numérotées** reconnaissables dès la 1re image : « Devine le jeu #2 », « Légendes du jeu #1 »,
  « Top 5 », « Doc Manette » (réparation), « Duel de consoles ». Même kicker et même accroche-type à chaque épisode.
- **Classements** en format « tier list » ou compte à rebours du n°5 au n°1 (le n°1 à la fin pour garder l'attention).
- **Commentaires** : demander une réponse précise (« Écris ton top 1 en commentaire »), jamais « like et abonne-toi ».
  Le 1er commentaire pose une question. Les commentaires pèsent plus que les abonnements dans l'algorithme.
- **Mots-clés** : titre YouTube et légende avec le nom du jeu ou de la console (recherche Shorts), 3 à 5 hashtags.
- **Actualité** : publier dans les 48 h d'une grosse sortie (GTA 6 le 19 nov.) rapporte nettement plus de vues.
- **Audio original** (voix ElevenLabs) : à garder, il est favorisé ; ne jamais reposter une vidéo avec un filigrane.
- Au bilan du dimanche : comparer la rétention moyenne (cible ≥ 65 % pour < 30 s) et les commentaires par vidéo,
  et garder les séries qui marchent le mieux.

## Leçons de l'analyse du 18 nov. 2026 (obligatoires, demande du propriétaire)

Analyse TikTok du 1er au 15 nov. : les posts avec #gta6 font ≈ 530 vues en moyenne contre ≈ 280 sans ;
le Top 5 de jeux peu connus (45 s) = 66 vues ; l'humour du quotidien a le meilleur taux de j'aime (7,8 %) ;
seul le quiz fait commenter ; presque aucun partage. Règles qui en découlent :

1. **Un nom très connu au Congo dans chaque vidéo** (GTA 6, PS5, manette PS5, EA Sports FC/FIFA, Call of Duty,
   Fortnite, Mortal Kombat, PES/eFootball) : dans l'accroche (titre de la scène 1), la 1re ligne de la légende,
   le titre YouTube et un hashtag. Jamais de vidéo construite autour de jeux peu connus localement
   (pas de classement de jeux indés ou de niche).
2. **Hashtags (5)** : le jeu ou la console vedette (#gta6 tant que GTA 6 est l'actu, au moins jusqu'au 6 déc.),
   #ps5, #kolwezi, #gamingrdc, + 1 tag de format (#humourgaming, #quizgaming, #reparationmanette…).
3. **Durée : 25 à 32 s, plafond strict.** Montage > 32 s → raccourcir les voix et re-rendre. Classement = 3 éléments
   maximum (pas 5).
4. **Humour = vie quotidienne à Kolwezi + jeu connu** (coupures de courant, la moto-taxi, le pote qui squatte la manette,
   la maman qui appelle en pleine partie de GTA 6…). C'est le format le plus aimé : en faire au moins 1 sur 4.
5. **Quiz = le jeu est nommé** dans le titre et les hashtags (« Vrai ou faux GTA 6 », « Devine le joueur EA FC ») ;
   seule la réponse reste cachée. Réponse demandée en un mot dans les commentaires.
6. **Appel au partage** dans la dernière scène et la légende : « Envoie ça à ton pote qui… » (cible : ≥ 1 partage
   par vidéo). La question pour les commentaires reste en 1er commentaire.
7. **Ponctualité** : la publication part à l'heure prévue ; un retard > 1 h se note dans le journal.
8. **Bilan du dimanche** : relever pour chaque vidéo vues, j'aime, commentaires et partages, puis comparer
   « nom connu / pas de nom connu » et « humour / info / quiz » pour confirmer ou corriger ces règles.

## Règles de contenu

- Vidéo verticale 4K 2160x3840 (copie 1080x1920 pour Instagram), 24 à 32 secondes, voix off française sur chaque scène.
- Scène 1 = accroche en moins de 2 s (question, chiffre, « attention », réaction forte).
- Ton : jeune, direct, tutoiement, français simple. Pas de vulgarité, pas de politique.
- Prix et disponibilités : UNIQUEMENT ceux de `produits.md`. Liste vide ou produit absent
  = ne citer aucun prix ni stock. Ne jamais inventer de promotion, de prix ou de date.
- Actualité : seulement des faits vérifiés par une recherche web le jour même.
- Aucun logo, personnage, jeu ou visuel protégé généré par IA ni téléchargé sur le web ; les vrais
  produits n'apparaissent que via les rushes de la boutique. Personnes fictives uniquement dans les
  clips IA, aucune ressemblance avec une vraie personne.
- Ne pas répéter un sujet publié dans les 10 derniers jours (voir `journal.md`).

## Qualité 4K (décision du propriétaire, 16 nov. 2026)

- **Clips IA : uniquement en mode `4k`** de Kling 3.0 (plus jamais `pro` ni `std`). Coût vérifié le
  16 nov. : **30 crédits par clip de 5 s** (au lieu de 8,75 en pro).
- **Vidéo publiée en 4K verticale 2160x3840** (montage automatique : textes capturés au double,
  un seul encodage final de haute qualité). Cause du flou constatée le 16 nov. : fichiers 1080p à
  ≈ 2,3 Mbit/s, compressés 4 à 5 fois jusqu'à YouTube. Les envois en 1440p ou plus reçoivent
  en général une meilleure compression sur YouTube.
- Le montage produit aussi `videos/AAAA-MM-JJ-1080.mp4` (1080x1920) pour Instagram, dont l'API
  Reels refuse plus de 1920 px de large. Tant qu'Instagram est déconnecté de Metricool, ne rien en faire ;
  une fois reconnecté, programmer Instagram dans une publication séparée avec ce fichier.
- Moins de clips par vidéo (budget) : les scènes sans clip passent en motion design (fond animé),
  le clip 4K va en priorité sur l'accroche (scène 1).

## Format d'une vidéo (moteur « motion »)

Ancien format « premium » N2 en clips pro (avant le 16 nov.), conservé pour mémoire ; depuis le
16 nov., niveaux K1 à K3 en clips 4K (voir « Budget ») :

| Scène | Durée | Contenu | Source | Crédits |
| --- | --- | --- | --- | --- |
| 1 Accroche | ~5 s | clip IA + titre | Kling 3.0 | 8,75 |
| 2 Contenu | ~5 s | clip IA + texte | Kling 3.0 | 8,75 |
| 3 Contenu | ~5 s | clip IA + texte | Kling 3.0 | 8,75 |
| 4 Contenu | ~5 s | clip IA + texte | Kling 3.0 | 8,75 |
| 5 Info clé | 4–6 s | liste, gros chiffre, comparatif sur fond animé | motion | 0 |
| Fin | ~5 s | NEXIS GAMING + adresse (automatique) | motion | 0 |
| Voix off | toute la vidéo | voix naturelle ElevenLabs, une piste par scène + fin | Higgsfield | ≈ 2 |

Niveaux supérieurs : N3 = la scène 5 devient aussi un clip IA (texte de l'info clé en bas) ;
N4 = N3 + accroche de 10 s (clip de 10 s, 17,5 au lieu de 8,75). Niveau inférieur N1 = 3 clips.

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

- generate_video_batch, une requête par clip du niveau choisi (K1 = 1, K2 = 2, K3 = 3) : model `kling3_0`, aspect_ratio `9:16`, duration 5,
  mode **`4k`**, sound `off`, use_unlim false. Avant : generate_video avec
  get_cost true pour vérifier le prix (30 pour 5 s en 4K) et balance pour le solde. Puis jobs_wait jusqu'à la fin.
- Style commun des prompts (en anglais) : vertical cinematic shot, night, small modern video game
  shop or gamer bedroom lit by cyan and magenta neon, young Black African people in casual
  streetwear (fictional), plain black consoles/controllers with no logos, screens showing only
  abstract colorful light, realistic, shallow depth of field, slow camera move.
  Toujours ajouter : « No text, no logos, no brand names, no recognizable game footage. »
- L'URL du résultat de chaque clip va dans le champ "clip" de sa scène.

### Montage

- Commit + push du spec : le workflow GitHub « Rendu vidéo » télécharge les clips, monte la vidéo
  en 4K (≈ 15 à 25 min) et pousse `videos/AAAA-MM-JJ.mp4` (+ `-1080.mp4`). Attendre avec
  `gh api repos/Ngandu-Moise/nexis-gaming-media/contents/videos/AAAA-MM-JJ.mp4` (toutes les 30 s,
  45 min maximum), puis `git pull`. Fichier limité à 95 Mo (réencodé automatiquement au-delà). Échec : lire le journal du run (outils GitHub Actions).
- Contrôle : extraire une image au milieu de chaque scène (ffmpeg) et les regarder. Refuser :
  mains ou visages déformés, logo ou texte parasite, élément protégé, texte illisible ou coupé.
- Clip refusé : le refaire une seule fois (nouveau prompt), repousser le spec. Second échec :
  retirer le "clip" de cette scène (fond animé). La vidéo sort quand même.
- Sans abonnement ou en cas de panne Higgsfield : vidéo sans clip (0 crédit), le noter.

## Budget de crédits : zéro crédit perdu (600 par cycle, du 3 au 2 du mois suivant)

Objectif : finir chaque cycle avec **moins de 1 crédit** non utilisé. Les crédits ne sont pas reportés.
Prix vérifiés : clip Kling 3.0 5 s en **4K = 30** (16 nov. 2026) ; image gpt_image_2_6 = 0,25 ;
voix ElevenLabs ≈ 2 par vidéo. Depuis le 16 nov., seuls les niveaux 4K ci-dessous sont utilisés
(N1 à N4 en clips pro : abandonnés).

| Niveau | Contenu | Crédits |
| --- | --- | --- |
| K0 | motion design sans clip + voix | 2 |
| K1 | 1 clip 4K (accroche) + voix | 32 |
| K2 | 2 clips 4K + voix | 62 |
| K3 | 3 clips 4K + voix | 92 |
| Reprise | 1 clip 4K refait | 30 |

Dans les règles ci-dessous, lire « 8,75 » (reprise) comme **30**, « 28,25 » (plus petit niveau
avec clips) comme **32**, « N4 » comme le niveau le plus élevé que permet le reste, et « monter /
descendre d'un niveau » sur l'échelle K0 → K3.

### Règle de calcul (chaque jour de publication, avant de générer)

1. S = solde (balance). V = vidéos restantes dans le cycle, celle du jour comprise
   (jours de publication jusqu'au 2 inclus, sans compter la vidéo de vidage).
2. Si V > 1 : budget du jour B = (S − 8,75) / V (8,75 = une reprise gardée en réserve).
   Choisir le niveau le plus élevé dont le coût ≤ B. Exception : un jour d'événement prévu au
   programme peut prendre N4 si S reste ≥ la cible du tableau ci-dessous moins 20.
3. Si V = 1 (dernière vidéo du cycle) : faire les reprises éventuelles, puis dépenser au niveau N4.
   Ensuite, si le reste ≥ 28,25 → vidéo de vidage le 2 du mois avec tout le reste (N1 à N4,
   + clips en plus, jusqu'à 6 clips / 35 s). Si 8,75 ≤ reste < 28,25 → ajouter des clips à la
   dernière vidéo. Reste < 8,75 → images de fond (0,25 l'une) pour les scènes « info » des vidéos
   suivantes (URL notées dans `journal.md`), jusqu'à reste < 0,5.
4. Comparer S après génération à la cible : écart > +20 → monter d'un niveau à la vidéo suivante ;
   écart < −20 → descendre d'un niveau et notifier le propriétaire.
5. Solde < 10 → aucun clip (voix seule si possible). Ne jamais acheter de crédits ni changer
   d'abonnement.

### Plan révisé en 4K (16 nov. 2026, solde 354,55)

| Date | Vidéo | Niveau | Crédits | Solde cible après |
| --- | --- | --- | --- | --- |
| 17 nov. (mar.) | Doc Manette : manette qui dérive, avant GTA 6 | K1 | 32 | 322,55 |
| 19 nov. (jeu.) | GTA 6 est sorti aujourd'hui (10 h) — événement | K2 | 62 | 260,55 |
| 21 nov. (sam.) | Quiz : « Vrai ou faux GTA 6 » (3 affirmations, réponse en 1 mot en commentaire) | K1 | 32 | 228,55 |
| 23 nov. (lun.) | Légendes du jeu #2 : de FIFA à EA Sports FC (jeu de foot très connu localement ; à confirmer au bilan du 22) | K1 | 32 | 196,55 |
| 25 nov. (mer.) | GTA 6 : premières notes et chiffres (sources vérifiées) | K1 | 32 | 164,55 |
| 27 nov. (ven.) | Humour : la vie quotidienne à Kolwezi pendant une partie de GTA 6 (ex. « juste une mission » à 2 h du matin) | K1 | 32 | 132,55 |
| 29 nov. (dim.) | Astuces : premiers réglages dans GTA 6 | K1 | 32 | 100,55 |
| 1er déc. (mar.) | Réparation PS5 et manette (dernière vidéo du cycle) | K3 | 92 | 8,55 |
| 2 déc. (mer.) | pas de vidage (reste < 32) : images de fond 0,25 | — | ≈ 8,55 | ≈ 0 |

Chaque reprise (30) est prise sur la vidéo du 1er déc. (K3 → K2). Cycles suivants (600 crédits,
≈ 15 vidéos) : budget ≈ 38 par vidéo, donc K1 en standard, K2 les jours d'événement.

### Ancien plan du cycle 3 nov. → 2 déc. 2026 en clips pro (remplacé le 16 nov.)

| Date | Vidéo | Niveau | Crédits | Solde cible après |
| --- | --- | --- | --- | --- |
| 7 nov. (sam.) | Devine le jeu en 3 indices | N2 | 37 | 567,45 |
| 9 nov. (lun.) | Histoire : la saga GTA, de 1997 à GTA 6 (J-10) | N2 | 37 | 530,45 |
| 11 nov. (mer.) | Top 5 des meilleurs jeux de 2026 (notes Metacritic/OpenCritic vérifiées le jour même, sans GTA 6 non sorti) — choix du propriétaire le 10 nov. | N1 (règle 4) | 28,25 | 493,45 |
| 13 nov. (ven.) | Humour : coupure de courant en pleine mission | N2 | 37 | 456,45 |
| 15 nov. (dim.) | Prépare ta console pour GTA 6 en 4 étapes | N2 | 37 | 419,45 |
| 17 nov. (mar.) | Manette qui dérive : répare-la avant GTA 6 | N2 | 37 | 382,45 |
| 19 nov. (jeu.) | GTA 6 est sorti aujourd'hui (10 h) | N4 | 54,5 | 327,95 |
| 21 nov. (sam.) | Quiz : vrai ou faux gaming | N3 | 45,75 | 282,20 |
| 23 nov. (lun.) | Histoire d'un jeu légendaire (choisi au bilan du 22) | N3 | 45,75 | 236,45 |
| 25 nov. (mer.) | Jeux phares : GTA 6, premières notes et chiffres une semaine après la sortie (sources vérifiées) | N3 | 45,75 | 190,70 |
| 27 nov. (ven.) | Humour gaming | N3 | 45,75 | 144,95 |
| 29 nov. (dim.) | Astuces : premiers réglages dans GTA 6 | N3 | 45,75 | 99,20 |
| 1er déc. (mar.) | Réparation PS5 et manette (dernière vidéo du cycle) | N4 | 54,5 | 44,70 |
| 2 déc. (mer.) | vidéo de vidage (reprises non utilisées) | selon reste | ≈ 44,70 | ≈ 0 |

Les 44,70 restant au 1er déc. = 4 reprises possibles (35) + 9,70. Chaque reprise faite réduit d'autant
la vidéo de vidage. Cycles suivants : refaire ce tableau au premier bilan du cycle avec la même règle.

## Programme du 7 au 20 novembre 2026

Détail (accroches, clips, légendes, plan B) : https://claude.ai/artifact/XbungjxD5QHa1WFoUB3hqD
Fil rouge : compte à rebours GTA 6. Sujets et niveaux : tableau « Plan du cycle » ci-dessus.
Chaque fait sur un jeu est revérifié le jour même ; le préchargement GTA 6 (annoncé au 12 nov. par
la presse) et la taille du jeu ne sont cités que s'ils sont officiels.

## Vidéo préparée à l'avance

Si `videos/AAAA-MM-JJ.mp4` du jour existe déjà (préparée la veille), ne rien générer : contrôler la vidéo puis la programmer
à l'heure prévue avec la légende notée dans `journal.md`.

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
