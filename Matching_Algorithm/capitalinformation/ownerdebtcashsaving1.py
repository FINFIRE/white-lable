from django.shortcuts import render,HttpResponse,redirect
from django.utils.safestring import mark_safe
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared
from iquestions.models import IQuestions1,IQuestions2
from registration.models import User,UserDetail,UserDetail2
from connections.models import Match_Data
from datetime import datetime
from django.contrib.auth.decorators import login_required
from ..models import Capital_Matches,Matches_Purchased,Letter_Response,Purchases


def ownerdebtcashsaving(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Owner Debt</b></u><br>

    Capital Type: Cash Savings</center></p>

    <p><b><u>Introduction</u></b><br>

   Owner debt through cash savings refers to capital invested into a business directly from the personal savings of the founder or owner. {n} fits that definition. Cash savings allow founders to retain full ownership and control while avoiding interest payments, external scrutiny, or dilution. According to the Global Entrepreneurship Monitor (GEM), over 70% of startups worldwide rely on personal savings as their first source of capital. In developing economies, including South Asia, this figure often exceeds 80%, reflecting limited access to formal financing. Owner-funded startups typically invest between $1,000 and $50,000 in initial capital, depending on the industry and personal financial capacity. While cash savings offer flexibility and independence, they also expose founders to personal financial risk, making careful planning essential.

    </p>

 

    <p><b><u>Definition of Capital Type</b></u><br>

    <br>1. Owner debt in the form of cash savings refers to funds personally accumulated by the business owner and injected into the business to finance startup or early operational activities. These funds may come from salaries, prior business income, inheritances, or long-term personal savings. Unlike external debt or equity financing, cash savings do not require repayment to third parties, interest obligations, or ownership dilution. The owner assumes full financial risk, and the capital is typically recorded as owner’s capital or shareholder loan depending on accounting treatment. Cash savings are often used to cover initial expenses such as registration costs, equipment purchases, marketing, rent, and early working capital needs. (Investopedia, n.d.)

<br>



    <br>2.  Cash savings are best suited for micro-enterprises, sole proprietorships, early-stage startups, and small service-based businesses with relatively low capital requirements. Businesses in consulting, freelancing, retail, food services, digital platforms, and creative industries often rely on owner savings due to their minimal upfront costs. This capital type is ideal for founders in the idea stage or pre-revenue phase, where external investors may be unwilling to invest due to high uncertainty. Entrepreneurs with strong personal financial discipline, low opportunity cost, and a clear path to early revenue generation benefit most from using cash savings. (OECD, 2022)

<br>

    <br>3. The use of personal savings as a source of business capital predates modern financial systems and remains the foundation of entrepreneurship globally. Historically, family wealth and personal savings were the primary means of financing trade and small enterprises before the emergence of banks and venture capital. Even with the growth of formal capital markets, owner-financed businesses remain dominant, particularly in emerging economies. During periods of economic uncertainty—such as the 2008 financial crisis and the COVID-19 pandemic—entrepreneurs increasingly relied on personal savings due to tightened credit conditions. Today, cash savings continue to play a critical role in bootstrapping startups and validating business models before seeking external funding. (World Bank, 2021)
	
<br>

    <br>4. Despite its advantages, using cash savings carries significant risks. The most critical risk is personal financial exposure, as business failure can directly impact the owner’s financial security, emergency funds, or family obligations. Over-investment of personal savings may lead to stress, burnout, or inability to cover personal expenses. Additionally, limited capital may restrict growth potential, marketing reach, or hiring capacity, slowing business scalability. Unlike institutional funding, cash savings do not come with mentorship, strategic guidance, or professional networks. There is also an opportunity cost, as funds invested in the business could have been used for alternative investments or long-term savings. (Small Business Administration, 2023)

<br>

    <br>5. 
To raise capital through cash savings, the owner must first assess personal financial readiness, including emergency reserves and risk tolerance. A clear business plan outlining startup costs, operating expenses, and expected cash flows is essential. Funds are typically transferred from personal accounts into the business account and recorded properly in accounting books. Depending on legal structure, the investment may be classified as owner’s equity or a shareholder loan. Maintaining financial discipline, budgeting, and tracking expenses is critical to ensure sustainability. Many founders use cash savings as seed capital and later transition to external funding once the business demonstrates traction, revenue, or market validation. (Entrepreneur.com, n.d.)

    </p>

                            

    <p><u><b>References</u></b><br>

    <br>Investopedia. (n.d.). Bootstrapping. <a href="https://www.investopedia.com">https://www.investopedia.com</a>

<br>

    <br>Global Entrepreneurship Monitor. (2023). Global Report. <a href="https://www.gemconsortium.org">https://www.gemconsortium.org</a>

<br>

    <br>OECD. (2022). Financing SMEs and Entrepreneurs. <a href=" https://www.oecd.org"> https://www.oecd.org</a>

<br>

    <br>World Bank. (2021). Entrepreneurship and Financial Inclusion. <a href="https://www.worldbank.org">https://www.worldbank.org</a>

<br>

    <br>U.S. Small Business Administration. (2023). Small Business Financing Guide.  <a href="https://www.sba.gov">https://www.sba.gov</a>

<br>

    <br>Entrepreneur.com. (n.d.). Using personal savings to start a business. <a href="https://www.entrepreneur.com">https://www.entrepreneur.com</a>

    </p>

                                                          

    <p><u><b>Legal Qualification Requirements</u></b>

<br>•	Legal Business Structure – Sole proprietorship, partnership, or incorporated entity
<br>•	Personal Ownership Proof – Founder must legally own the invested funds
<br>•	Tax Compliance – Personal and business tax obligations must be met
<br>•	Separate Bank Accounts – Clear distinction between personal and business finances
<br>•	Accounting Records – Proper documentation of capital contribution
<br>•	No Fraudulent Sources – Funds must come from legitimate, traceable income
<br>•	Business Registration – Company must be registered if required by law
<br>•	Compliance with Local Laws – Adherence to national business regulations


    </p>

                                

    <p><b><u>Supporting Document List</u></b>
<br>•	Personal Bank Statements – Evidence of available savings
<br>•	Business Registration Certificate – Proof of legal operation
<br>•	Capital Contribution Record – Documentation of funds invested
<br>•	Business Plan – Outline of fund usage and growth strategy
<br>•	Cash Flow Projections – Expected inflows and outflows
<br>•	Owner’s Declaration – Statement confirming ownership of funds
<br>•	Accounting Records – Ledger entries showing capital injection
<br>•	Tax Clearance Certificate – If required by local authorities

    </p>
        """)

    introduction = mark_safe(introduction.format(n=name))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def ownerdebtcashsavingfaq(request):
    introduction = mark_safe("""<p><b><center>Capital Market: Owner Debt<br>

    Cash Savings</center></b></p>                       

    <p><center><u><b>Frequently Asked Question</u></b></center></p>

                            

    <p><u><b>1. What is owner debt using cash savings?</u></b><br>

    •Answer: Owner debt using cash savings refers to funding a business by the founder or owner through their personal savings, which are injected into the company as a loan rather than equity. The business records this amount as a liability, meaning the company is obligated to repay the owner under agreed terms.</p>

                            

    <p><u><b>2. How does owner debt differ from equity funding?</u></b><br>

    • Answer: Unlike equity funding, owner debt does not dilute ownership or control of the business. The owner remains the full or majority owner while acting as a lender. The business must repay the debt, whereas equity funding does not require repayment but reduces ownership percentage.</p>

                            

    <p><u><b>3. What types of businesses are best suited for owner debt funding?</u></b><br>

    •Answer: Owner debt is best suited for early-stage startups, small businesses, and sole proprietorships that need initial capital for setup, operations, or working capital. It is especially common in businesses that are pre-revenue or not yet attractive to external investors. </p>                            

                            

    <p><u><b>4. How much capital can be provided through owner cash savings?</u></b><br>

    • Answer: The amount depends entirely on the owner’s financial capacity and risk tolerance. Typically, owner debt ranges from small amounts used for initial setup costs to larger contributions that cover early operational expenses, such as rent, inventory, or equipment.</p>

                            

    <p><u><b>5. How quickly can the business access funds from owner cash savings?</u></b><br>

    •Answer: Funds from owner cash savings are immediately available once the owner transfers the money into the business account. There are no approval processes, legal delays, or third-party negotiations involved, making this one of the fastest funding options. </p>

                            

    <p><u><b>6. What are the costs associated with using owner debt?</u></b><br>

    • Answer: There are no application fees, legal fees, or investor commissions. However, the owner bears the opportunity cost of using personal savings and the financial risk if the business fails. If interest is charged, it becomes an expense for the business.</p>

                            

    <p><u><b>7. 7. Does owner debt require repayment with interest?</u></b><br>

    • Answer: Owner debt may or may not include interest, depending on how it is structured. Some owners choose to charge interest to reflect market conditions, while others keep it interest-free. The repayment terms should be clearly documented to avoid future disputes.</p>

                            

    <p><u><b>8. How is owner debt recorded in the financial statements?</u></b><br>

    • Answer: Owner debt is recorded as a liability on the balance sheet, typically under “Loans from Owner” or “Shareholder Loans.” Any repayments reduce the liability, and interest payments are recorded as an expense in the income statement.</p>

                            

    <p><u><b>9. Can owner debt affect future external funding opportunities?</u></b><br>

    • Answer: Yes, owner debt can influence future funding decisions. Investors and lenders may evaluate the size and terms of owner debt to assess financial risk. However, reasonable owner debt often demonstrates founder commitment and can positively signal confidence in the business.</p>

                            

    <p><u><b>10. Can owner debt be converted into equity later?</u></b><br>

    • Answer: Yes, owner debt can be converted into equity if both the owner and the business agree. This is commonly done during later funding rounds to clean up the balance sheet or align ownership structure before bringing in external investors.</p>
                        

    <p><u><b>11. What are the key advantages of owner debt using cash savings?</u></b><br>

    • Answer: The main advantages include full control retention, fast access to capital, flexibility in repayment terms, and no dependence on external parties. It also demonstrates strong founder commitment and belief in the business.</p>

                        

    <p><u><b>12. What are the risks of funding a business through owner cash savings?</u></b><br>

    • Answer: The primary risks include personal financial loss, lack of diversification, and potential cash flow strain if the business cannot repay the loan. Over-reliance on personal savings can also limit the owner’s personal financial security.</p>

                        

    <p><u><b>13. How does owner debt compare to bank loans or external debt?</u></b><br>

    • Answer: Owner debt is more flexible and less formal than bank loans, with no collateral or strict repayment schedules unless defined by the owner. However, unlike bank loans, it does not help build the company’s credit history with external financial institutions.</p>

                        

    <p><u><b>14. Can owner debt be used alongside other funding sources?</u></b><br>

    • Answer: Yes, owner debt can be combined with other funding sources such as accelerators, angel investors, or bank loans. It is often used as initial capital before external funding is secured or as bridge financing during early stages.</p>

                        

    <p><u><b>15. How can owner debt be structured effectively?</u></b><br>

    • Answer: Owner debt should be documented with clear terms, including loan amount, repayment schedule, interest rate (if any), and conversion options. Proper documentation ensures transparency, supports financial reporting, and avoids legal or accounting complications in the future.</p>
    """)



    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)

def ownerdebtcashsavingtwelve(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    entity = EQuestions2.objects.get(user=request.user).Selected_Option
    stage = EQuestions1.objects.get(user=request.user).Selected_Option
    preraise = EQuestions3.objects.get(user=request.user).Selected_Option
    premarket = EQuestions4.objects.get(user=request.user).Selected_Options
    raisegoal = EQuestions5.objects.get(user=request.user).Selected_Option
    useoffund = EQuestions7.objects.get(user=request.user).Selected_Options
    enterprisecost = EQuestions8.objects.get(user=request.user).Selected_Option2
    tranch = EQuestions6.objects.get(user=request.user).Selected_Option
    rounds = EQuestions6.objects.get(user=request.user).Selected_Options
    upfrontcost = EQuestions.objects.get(user=request.user).Selected_Option
    upfronttime = EQuestions.objects.get(user=request.user).Selected_Option2
    introduction = """<center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Owner Debt</b></u><br>

    Capital Type: Cash Savings</p></center>

 

    <p><b><u>1 - Stage of Development Assessment</b></u><br>

    Owner debt financed through personal cash savings is most suitable at the idea stage, pre-revenue, or very early revenue stage. At this stage, the business may not qualify for external financing, and the owner relies on personal resources to start operations, test the business concept, and cover initial setup costs. This form of capital is especially common during business formation and early market entry.

    </p>

   

    <p><b><u>2 - Entity Type Assessment</b></u><br>

Owner debt using cash savings can be applied to all entity types, including sole proprietorships, partnerships, LLCs, and corporations. It is particularly common in sole proprietorships and partnerships, where the owner and business finances are closely linked. For LLCs and corporations, owner cash injections are often structured as shareholder loans to maintain clarity between personal and business finances.

    </p>

   

    <p><b><u>3 - Pre Capital Assessment</b></u><br>

There are no formal restrictions on pre-existing capital when using owner debt from cash savings. This capital source is typically used when little to no external funding has been raised. Even businesses with some prior funding may still use owner debt to bridge short-term gaps or reduce reliance on external lenders.

    </p>

 

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>

Since cash savings are internally sourced, there are no capital market restrictions. This form of funding does not involve equity markets, venture capital, or debt markets, making it highly flexible. However, excessive reliance on owner debt may limit future investor interest if the business appears undercapitalized or overly dependent on personal funds.

    </p>

 

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>

Owner debt through cash savings is usually limited in size, depending on the owner’s financial capacity. It is best suited for small to moderate capital needs such as startup costs, working capital, or short-term operational expenses. For long-term scaling, this capital is often supplemented with loans, equity investment, or retained earnings.

    </p>

   

    <p><b><u>6 - Capital Round Assessment</b></u><br>

This capital type does not follow formal funding rounds like pre-seed or seed. Instead, it is typically injected as needed, either as a one-time contribution or multiple small infusions. It is most aligned with the pre-seed or bootstrapping phase of the business lifecycle.

    </p>

 

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>

Owner debt from cash savings is usually provided in a single tranche or flexible multiple tranches based on business needs. The timing is fully controlled by the owner, allowing quick responses to cash flow requirements without external approval or milestones.

    </p>

   

    <p><b><u>8 - Use of Funds Assessment</b></u><br>

Funds from owner cash savings are generally used for:
<br>•	Business registration and legal setup
<br>•	Initial inventory or equipment
<br>•	Rent and utilities
<br>•	Marketing and early customer acquisition
<br>•	Day-to-day operating expenses
    
</p>

   

    <p><b><u>9 - Risk Assessment</b></u><br>

Owner debt carries high personal financial risk, as the owner’s savings are directly exposed to business failure. There is no risk-sharing with external parties. If the business fails, the owner may lose personal financial security. However, there is no dilution of ownership or external control risk.

    </p>

 

    <p><b><u>10 - Capital Cost Assessment</b></u><br>

The explicit cost of capital is low to zero, as there is typically no interest paid to external parties. However, the opportunity cost can be high, as personal savings could have been invested elsewhere. The implicit risk-adjusted cost is significant due to full personal exposure.

    </p>

   

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>

There are no transaction or application costs associated with using personal cash savings. However, indirect costs may include reduced personal liquidity, emergency fund depletion, and potential personal borrowing needs in the future if savings are exhausted.

    </p>

 

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>

Timing is the fastest among all capital types. Funds are immediately available, allowing the business to act quickly on opportunities or urgent needs. There is no approval process, documentation delay, or third-party dependency, making this ideal for urgent or early-stage funding requirements.
</p>"""

    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))

    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)