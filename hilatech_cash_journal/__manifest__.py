{
    'name': 'Cash Journal - Journal de Caisse',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Cash Management',
    'sequence': 0,
    'license': 'LGPL-3',
    'author': 'Hilatech',
    'website': 'https://hilatech.co',
    'icon': '/hilatech_cash_journal/static/description/icon.png',
    'support': 'support@hilatech.com',

    'summary': 'Gestion du flux d\'entrée et sortie de caisse avec relevés mensuels et clôtures quotidiennes',

    'description': """
╔═══════════════════════════════════════════════════════════════════════════╗
║              CASH JOURNAL - JOURNAL DE CAISSE                             ║
╚═══════════════════════════════════════════════════════════════════════════╝

🎯 Système complet de gestion du flux de caisse pour entreprises.

═══════════════════════════════════════════════════════════════════════════
📋 FONCTIONNALITÉS PRINCIPALES:
═══════════════════════════════════════════════════════════════════════════

✅ RELEVÉS MENSUELS:
   • Création automatique des relevés mensuels
   • Solde initial et solde final (calculé automatiquement)
   • Numérotation séquencielle: JRN/ANNÉE/NUMÉRO
   • Traçabilité des responsables

✅ OPÉRATIONS QUOTIDIENNES:
   • Enregistrement des entrées et sorties
   • Date, description, bénéficiaire, montant signé
   • Montant positif = entrée, négatif = sortie
   • Calcul automatique du solde journalier

✅ WORKFLOW QUOTIDIEN:
   • Bouton "Ouvrir la caisse" : active l'enregistrement des opérations
   • Saisie des opérations du jour
   • Bouton "Clôturer la caisse du jour" : gèle les opérations du jour
   • Calcul automatique du solde final journalier
   • Bouton "Ouvrir la caisse" pour le prochain jour

✅ CLÔTURE MENSUELLE:
   • Bouton "Clôturer le relevé mensuel" : fermeture définitive
   • Empêche toute modification ultérieure
   • Historique permanent

✅ CONTRÔLE D'ACCÈS:
   • Deux rôles : Utilisateur (saisie) et Gestionnaire (clôture)
   • Permissions granulaires par modèle
   • Piste d'audit complète

═══════════════════════════════════════════════════════════════════════════
📊 MODÈLES DE DONNÉES:
═══════════════════════════════════════════════════════════════════════════

RELEVÉ MENSUEL (cash.journal.report):
• Numéro séquentiel (auto-généré)
• Date du mois
• Solde initial
• Solde final (calculé)
• État du relevé (Ouvert/Clôturé)
• État de la caisse du jour (Ouverte/Fermée)
• Liste des opérations
• Responsable et entreprise

OPÉRATION (cash.journal.operation):
• Date de l'opération
• Description/Motif
• Reçu par (Partner/Employé)
• Montant (signé: +entrée, -sortie)
• Statut de verrouillage

═══════════════════════════════════════════════════════════════════════════
🎓 CAS D'USAGE:
═══════════════════════════════════════════════════════════════════════════

📍 Restaurants & Hôtels
   → Gestion quotidienne de la caisse
   → Rapprochement de caisse en fin de journée
   → Suivi des versements et dépenses

📍 Commerces de Détail
   → Enregistrement des entrées/sorties
   → Contrôle de stock monétaire
   → Audit de caisse régulier

📍 Services & Prestations
   → Gestion des encaissements
   → Traçabilité financière
   → Rapports pour la comptabilité

═══════════════════════════════════════════════════════════════════════════
    """,

    'depends': [
        'base',
        'account',
        'mail',
    ],

    'data': [
        'security/cash_journal_security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/cash_journal_views.xml',
        'report_template.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'images':['static/description/banner.gif']
}
