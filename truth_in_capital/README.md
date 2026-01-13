# Truth in Capital - Task Management

## Overview

This module automatically creates capital type records and associated tasks for users when they use the Match or PDF functions in the Matching Algorithm.

## Features

### Automatic Task Creation
- When a user goes through the matching process (Match function) or generates a PDF, a capital type record is automatically created
- Associated tasks are automatically created based on the capital type
- Tasks are copied from the `rominadmin` user's template tasks for the same capital type

### Task Templates
- The `rominadmin` user serves as a template for all capital types
- Each capital type has specific, relevant tasks with appropriate hours and precedence
- If no `rominadmin` tasks exist, standard default tasks are created

## Setup

### 1. Initialize rominadmin Tasks
Run the management command to set up template tasks:

```bash
python manage.py setup_rominadmin_tasks
```

This will:
- Create the `rominadmin` user if it doesn't exist
- Create capital type records for all available capital types
- Create specific tasks for each capital type

### 2. Automatic Task Creation
The system automatically:
- Creates capital type records when users use Match/PDF functions
- Copies tasks from `rominadmin` template for the same capital type
- Falls back to standard tasks if no template exists

## Capital Types and Default Tasks

All 17 capital types use the same comprehensive set of 19 standard tasks:

### Standard Tasks for All Capital Types

#### Phase 0 (Precedence 0)
1. **Finfire Report - Capital Type** (4 hours) - FINFIRE Staff Review & Scope of Work
2. **Financial Model, forecast, pro forma** (20 hours) - Intermediary Services Scope of Work

#### Phase 1 (Precedence 1)
3. **Due Diligence Checklist Documents** (4 hours) - FINFIRE Staff Review & Scope of Work
4. **Historical Financials (P & L, BS, CF, Aging)** (1 hour) - FINFIRE Staff Review & Scope of Work
5. **Tax Returns (Up to 2 years, if applicable)** (1 hour) - FINFIRE Staff Review & Scope of Work
6. **Business Valuation (Equity only)** (20 hours) - Intermediary Services Scope of Work
7. **Cap Table, Use of Funds, & Capitalization Plan** (5 hours) - Intermediary Services Scope of Work

#### Phase 2 (Precedence 2)
8. **Executive Summary Including Exit Strategy** (2 hours) - FINFIRE Staff Review & Scope of Work
9. **Presentation Deck** (10 hours) - FINFIRE Staff Review & Scope of Work
10. **Business Model Canvas** (2 hours) - FINFIRE Staff Review & Scope of Work
11. **Resume of Founder/CEO Primary Leader** (1 hour) - FINFIRE Staff Review & Scope of Work
12. **Application (If Applicable)** (6 hours) - FINFIRE Staff Review & Scope of Work
13. **Presentation Video (From the AI Deep Dive)** (10 hours) - Intermediary Services Scope of Work
14. **Offering Documents** (25 hours) - Intermediary Services Scope of Work

#### Phase 3 (Precedence 3)
15. **Quality Assurance Checklist (Including AI)** (3 hours) - FINFIRE Staff Review & Scope of Work
16. **Capital Match List Generated** (10 hours) - FINFIRE Staff Review & Scope of Work

#### Phase 4 (Precedence 4)
17. **Investor Marketing Campaign** (20 hours) - Intermediary Services Scope of Work
18. **Investor Relations** (20 hours) - Intermediary Services Scope of Work
19. **Progress Reports** (12 hours) - Intermediary Services Scope of Work

### Capital Types
- Accelerator
- Bonds
- Bootstrapped
- Commercial Banking
- Cryptocurrency
- Factoring
- Grants
- Hedge Funds
- Incubator
- Investment Banking
- Private Debt
- Private Equity Securities
- Royalty Financing
- Small Business Administration (SBA)
- Third Party Corporate Credit
- Tokenization
- Venture Capital

All capital types will have identical task structures, making the system consistent and standardized across all capital markets. The tasks are organized in 5 phases with a total of 19 tasks covering the complete capital raising process.

## Usage

### For Developers
The functionality is automatically triggered when:
1. User calls the `Match` function
2. User calls the `pdf` function
3. User calls the `word` function

### Manual Task Creation
You can manually ensure rominadmin tasks exist:

```python
from truth_in_capital.utils import ensure_rominadmin_tasks_exist

# This will create rominadmin tasks if they don't exist
ensure_rominadmin_tasks_exist()
```

### Getting Template Tasks
You can get tasks for a specific capital type:

```python
from truth_in_capital.utils import get_rominadmin_tasks_for_capital_type

# Get tasks for Venture Capital
tasks = get_rominadmin_tasks_for_capital_type('Venture Capital')
```

## Models

### TruthCapitalType
- Links users to their capital types
- One capital type per user (enforced by unique constraint)

### Task
- Associated with a capital type
- Contains task name, max hours, type, and precedence
- Ordered by precedence

## Task Types
- **FINFIRE Staff Review & Scope of Work**: Internal analysis and preparation tasks
- **Intermediary Services Scope of Work**: External services and networking tasks

## Error Handling
- If rominadmin tasks don't exist, standard default tasks are created
- All operations include try-catch blocks to prevent crashes
- Detailed error logging for debugging
