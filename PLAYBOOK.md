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
  19 novembre sur PS5 et Xbox Series X|S). Le 19 novembre : « GTA 6 est sorti aujourd'hui ».
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

## Règles de contenu

- Vidéo verticale 1080x1920, 24 à 32 secondes, voix off française sur chaque scène.
- Scène 1 = accroche en moins de 2 s (question, chiffre, « attention », réaction forte).
- Ton : jeune, direct, tutoiement, français simple. Pas de vulgarité, pas de politique.
- Prix et disponibilités : UNIQUEMENT ceux de `produits.md`. Liste vide ou produit absent
  = ne citer aucun prix ni stock. Ne jamais inventer de promotion, de prix ou de date.
- Actualité : seulement des faits vérifiés par une recherche web le jour même.
- Aucun logo, personnage, jeu ou visuel protégé généré par IA ni téléchargé sur le web ; les vrais
  produits n'apparaissent que via les rushes de la boutique. Personnes fictives uniquement dans les
  clips IA, aucune ressemblance avec une vraie personne.
- Ne pas répéter un sujet publié dans les 10 derniers jours (voir `journal.md`).

## Format d'une vidéo (moteur « motion »)

Format standard « premium » (niveau N2, voir « Budget ») :

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

- generate_video_batch, une requête par clip du niveau choisi (N1 = 3, N2 = 4, N3/N4 = 5) : model `kling3_0`, aspect_ratio `9:16`, duration 5,
  mode `pro`, sound `off`, use_unlim false (accroche N4 : duration 10). Avant : generate_video avec
  get_cost true pour vérifier le prix (8,75 pour 5 s, 17,5 pour 10 s) et balance pour le solde. Puis jobs_wait jusqu'à la fin.
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

## Budget de crédits : zéro crédit perdu (600 par cycle, du 3 au 2 du mois suivant)

Objectif : finir chaque cycle avec **moins de 1 crédit** non utilisé. Les crédits ne sont pas reportés.
Prix vérifiés le 6 nov. 2026 : clip Kling 3.0 5 s = 8,75 ; 10 s = 17,5 ; image gpt_image_2_6 = 0,25 ;
voix ElevenLabs ≈ 2 par vidéo.

| Niveau | Contenu | Crédits |
| --- | --- | --- |
| N1 | 3 clips + voix | 28,25 |
| N2 premium (standard) | 4 clips + voix | 37 |
| N3 tout IA | 5 clips + voix | 45,75 |
| N4 événement | accroche 10 s + 4 clips + voix | 54,5 |
| Reprise | 1 clip refait | 8,75 |

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

### Plan du cycle 3 nov. → 2 déc. 2026 (solde 604,45 le 6 nov.)

| Date | Vidéo | Niveau | Crédits | Solde cible après |
| --- | --- | --- | --- | --- |
| 7 nov. (sam.) | Devine le jeu en 3 indices | N2 | 37 | 567,45 |
| 9 nov. (lun.) | Histoire : la saga GTA, de 1997 à GTA 6 (J-10) | N2 | 37 | 530,45 |
| 11 nov. (mer.) | GTA 6 J-8 : ce qui est confirmé | N2 | 37 | 493,45 |
| 13 nov. (ven.) | Humour : coupure de courant en pleine mission | N2 | 37 | 456,45 |
| 15 nov. (dim.) | Prépare ta console pour GTA 6 en 4 étapes | N2 | 37 | 419,45 |
| 17 nov. (mar.) | Manette qui dérive : répare-la avant GTA 6 | N2 | 37 | 382,45 |
| 19 nov. (jeu.) | GTA 6 est sorti aujourd'hui (10 h) | N4 | 54,5 | 327,95 |
| 21 nov. (sam.) | Quiz : vrai ou faux gaming | N3 | 45,75 | 282,20 |
| 23 nov. (lun.) | Histoire d'un jeu légendaire (choisi au bilan du 22) | N3 | 45,75 | 236,45 |
| 25 nov. (mer.) | Top 5 des meilleurs jeux de 2026 (sources vérifiées) | N3 | 45,75 | 190,70 |
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
