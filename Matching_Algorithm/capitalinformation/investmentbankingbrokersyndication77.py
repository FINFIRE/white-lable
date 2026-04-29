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

def investmentbankingbrokersyndication(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Investment Banking</b></u><br>
    Capital Type: Broker Syndication </center></p>
    <p><b><u>Introduction</u></b><br>
    Broker Syndication is ideal for issuers seeking to raise capital by distributing securities through a coordinated group of brokers or dealer firms rather than a single underwriter. It is designed so that multiple brokers collectively market, place, and sell securities to their respective investor networks, expanding distribution reach while sharing placement responsibility. {n} fits that definition. In 2026, broker syndication remains a widely used capital-raising mechanism for private placements, real estate offerings, structured products, and smaller public issuances. Investment banks and broker-dealers form syndicates to access diversified investor bases, improve execution certainty, and manage distribution risk across multiple channels. While broker syndication enhances market reach and capital access, it introduces coordination, compliance, and reputational risk. Issuers must manage consistent disclosures, broker compensation structures, and regulatory compliance across all syndicate participants.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. Broker Syndication is a capital distribution structure in which an issuer engages multiple brokers or broker-dealers to collectively place securities with investors, typically under a syndicate or selling-group arrangement. (Corporate Finance Institute, 2026)<br><br>
    2. Broker-syndicated offerings occupy a defined role within the Investment Banking distribution framework, where each broker acts as an intermediary rather than a principal investor. Securities may be equity, debt, or hybrid instruments, depending on the offering. (U.S. Securities and Exchange Commission, 2025)<br><br>
    3. Legally, broker syndication is governed by Syndicate Agreements or Selling Agreements that define allocation rights, commissions, disclosure responsibilities, and regulatory obligations. These arrangements must comply with securities laws, FINRA rules, and suitability standards. (FINRA, 2025)<br><br>
    4. From a risk perspective, broker syndication introduces execution, compliance, and coordination risk. Inconsistent disclosures, unsuitable sales practices, or broker misconduct can expose issuers and lead managers to regulatory enforcement and investor claims. (S&P Global Ratings, 2025)<br><br>
    5. From an accounting and process standpoint, broker-syndicated offerings record capital raised as Equity or Debt Proceeds, with placement fees and commissions expensed or capitalized according to accounting standards. Syndication enables broader distribution but requires rigorous oversight and centralized compliance management. (Deloitte, 2025)
    </p>
    <p><u><b>References</u></b><br>
    Corporate Finance Institute (CFI). (2026). Capital Markets Distribution and Syndication. https://corporatefinanceinstitute.com/resources/credit-analysis<br>
    U.S. Securities and Exchange Commission (SEC). (2025). Broker-Dealer Regulation. https://www.sec.gov<br>
    Financial Industry Regulatory Authority (FINRA). (2025). Selling Group and Syndicate Rules. https://www.finra.org<br>
    S&P Global Ratings. (2025). Execution Risk in Capital Markets Transactions. https://www.spglobal.com/ratings<br>
    Deloitte. (2025). Accounting for Capital Raising and Placement Fees. https://www2.deloitte.com/capital-markets
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    • Issuer Eligibility – Corporate, fund, or project issuer<br>
    • Broker-Dealer Registration – FINRA/SEC-registered participants<br>
    • Syndicate or Selling Agreement – Defined roles and compensation<br>
    • Disclosure Documentation – Prospectus or offering memorandum<br>
    • Suitability & Sales Practice Compliance – Investor protection rules<br>
    • Regulatory Filings – SEC and FINRA requirements<br>
    • Compensation Disclosure – Placement fees and commissions<br>
    • Ongoing Supervision – Lead manager oversight
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    • Syndicate or Selling Agreement – Broker participation terms<br>
    • Engagement Letter – Lead arranger mandate<br>
    • Offering Memorandum / Prospectus – Investor disclosures<br>
    • Broker-Dealer Agreements – Regulatory confirmations<br>
    • Compensation Schedule – Fees and commissions<br>
    • Marketing Materials – Approved investor communications<br>
    • Compliance Certifications – Sales practice adherence<br>
    • Board Resolutions – Authorization to raise capital
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def investmentbankingbrokersyndicationfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Investment Banking <br>
    Broker Syndication</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is broker syndication?</u></b><br>
    • Answer: Broker syndication is a capital-raising process where multiple brokers or financial institutions work together to distribute a securities offering to investors.
    </p>
    <p><u><b>2. Who participates in a broker syndication?</u></b><br>
    • Answer: Participants typically include lead underwriters, co-managers, selling group members, and investment banks or broker-dealers.
    </p>
    <p><u><b>3. When is broker syndication typically used?</u></b><br>
    • Answer: It is used for large or complex offerings where a single broker cannot efficiently place the entire issue.
    </p>
    <p><u><b>4. How does broker syndication work?</u></b><br>
    • Answer: A lead broker structures the deal and allocates portions of the offering to syndicate members, who then sell to their investor networks.
    </p>
    <p><u><b>5. What types of securities are syndicated?</u></b><br>
    • Answer: Securities may include equity, corporate bonds, municipal bonds, asset-backed securities, or structured products.
    </p>
    <p><u><b>6. What is the role of the lead broker in a syndication?</u></b><br>
    • Answer: The lead broker manages pricing, regulatory filings, marketing, allocation, and overall execution of the offering.
    </p>
    <p><u><b>7. How are underwriting risks shared in a syndication?</u></b><br>
    • Answer: Risk is shared among syndicate members based on their allocated commitments.
    </p>
    <p><u><b>8. How are fees structured in broker syndications?</u></b><br>
    • Answer: Fees are divided among syndicate members and typically include underwriting, management, and selling concessions.
    </p>
    <p><u><b>9. Are broker syndications regulated?</u></b><br>
    • Answer: Yes, they are subject to securities regulations, exchange rules, and broker-dealer compliance requirements.
    </p>
    <p><u><b>10. What are the benefits of broker syndication for issuers?</u></b><br>
    • Answer: Benefits include broader investor reach, risk sharing, and efficient capital distribution.
    </p>
    <p><u><b>11. What are the benefits for brokers in a syndication?</u></b><br>
    • Answer: Brokers gain access to larger deals, shared risk, and fee participation.
    </p>
    <p><u><b>12. What are the risks associated with broker syndication?</u></b><br>
    • Answer: Risks include market volatility, coordination challenges, unsold allocations, and regulatory exposure.
    </p>
    <p><u><b>13. How does broker syndication differ from sole underwriting?</u></b><br>
    • Answer: Syndication spreads risk and distribution across multiple brokers, while sole underwriting concentrates responsibility in one firm.
    </p>
    <p><u><b>14. Who typically uses broker syndication?</u></b><br>
    • Answer: Corporations, governments, municipalities, and large issuers commonly use broker syndication.
    </p>
    <p><u><b>15. When should an issuer consider broker syndication?</u></b><br>
    • Answer: An issuer should consider broker syndication when raising large amounts of capital or targeting diverse investor groups.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def investmentbankingbrokersyndicationtwelve(request):
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
    introduction = """
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Investment Banking</b></u><br>
    Capital Type: Broker Syndication</p></center>
    <p><b><u>1 – Stage of Development Assessment</u></b><br>
    Broker syndication is best suited for growth-stage to mature companies that have a defined capital need, established operations, and sufficient traction to attract multiple investors or lenders. While not appropriate for very early-stage startups, this structure is commonly used by companies that are beyond initial proof-of-concept and ready to access broader capital networks.
    </p>
    <p><b><u>2 – Entity Type Assessment</u></b><br>
    C-Corporations and LLCs are the most common entity types for broker-syndicated transactions, as these structures support standardized securities issuance, debt placement, and investor protections. Sole proprietorships are generally not suitable due to regulatory, compliance, and scale constraints.
    </p>
    <p><b><u>3 – Pre-Capital Assessment</u></b><br>
    Companies utilizing broker syndication typically have some prior capitalization, including equity investment, revenue history, or existing debt. Brokers rely on a credible operating history, financial disclosures, and a clear capital story to syndicate the opportunity across multiple investors or lenders.
    </p>
    <p><b><u>4 – Pre-Capital Market Type Assessment</u></b><br>
    Broker syndication operates within the private and semi-institutional capital markets and is facilitated by licensed investment banks, broker-dealers, and placement agents. Capital is sourced from family offices, private investors, funds, and institutional participants aggregated through broker networks.
    </p>
    <p><b><u>5 – Planned Total Capital to Raise Assessment</u></b><br>
    Capital raised through broker syndication commonly ranges from several million to hundreds of millions of dollars, depending on deal structure, market appetite, and broker reach. Syndication enables larger raises by distributing risk across multiple participants.
    </p>
    <p><b><u>6 – Capital Round Assessment</u></b><br>
    Broker-syndicated financings are not inherently tied to traditional venture capital rounds. They may be structured as equity raises, debt placements, hybrid instruments, or recapitalizations, depending on issuer needs and investor demand.
    </p>
    <p><b><u>7 – Tranche Schedule Assessment</u></b><br>
    Capital may be raised in a single close or through multiple closes as commitments are aggregated from syndicate participants. Rolling or staged closes are common to accommodate varying investor timelines and allocation sizes.
    </p>
    <p><b><u>8 – Use of Funds Assessment</u></b><br>
    Proceeds are typically used for growth expansion, acquisitions, refinancing, working capital, or strategic initiatives. Use of funds is disclosed to syndicate participants and may be governed by offering terms and covenants.
    </p>
    <p><b><u>9 – Risk Assessment</u></b><br>
    Risk to investors includes issuer performance risk, liquidity risk, and structural complexity due to multi-party participation. For issuers, risks include execution risk, disclosure obligations, and dependence on broker effectiveness and market conditions.
    </p>
    <p><b><u>10 – Capital Cost Assessment</u></b><br>
    The cost of capital includes broker commissions, placement fees, potential dilution or interest expense, and investor terms negotiated through the syndicate. While syndication expands access, it can increase overall transaction costs.
    </p>
    <p><b><u>11 – Up Front Cost Assessment</u></b><br>
    Upfront costs are moderate to high and include broker or placement agent fees, legal and offering documentation, due diligence preparation, and compliance expenses. Costs scale with transaction size and complexity.
    </p>
    <p><b><u>12 – Timing to Capital Assessment</u></b><br>
    Timing to capital typically ranges from one to three months, depending on broker engagement, investor response, diligence requirements, and market conditions.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
