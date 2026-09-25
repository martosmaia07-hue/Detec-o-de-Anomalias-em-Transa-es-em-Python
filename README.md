# 📊 Relatório de Experiência do Cliente (CX) & Análise de Negócios: Pós-Atualização do App Bancário

> **Contexto:** Análise quantitativa e qualitativa de 600 interações de feedback (NPS, CSAT e reviews das lojas digitais) coletadas após o último *release* do aplicativo móvel de serviços bancários. Documento elaborado para apoiar a diretoria de Produtos e a equipe de Desenvolvimento de Software na priorização de *hotfixes* e melhorias de UX/UI.

---

## 📈 Resumo Executivo

A última atualização do aplicativo gerou uma retração severa nas notas das lojas digitais (App Store e Google Play), impactando diretamente os índices de satisfação e retenção. Os dados apontam que **89,8% das avaliações recentes são negativas ou neutras**, concentradas em falhas críticas de estabilidade técnica e fricção na jornada do usuário.

### Tabela Comparativa: Gargalos por Volume de Reclamações

| Categoria Afetada | Volume de Reclamações | % do Total de Queixas | Nota Média | Principais Sintomas / Relatos |
| :--- | :--- | :--- | :--- | :--- |
| **Login** | 191 | 35,4% | 1.50 / 5.0 | Erros de autenticação (ex: Erro 403), falhas na biometria e *crashes* ao abrir o app. |
| **Transferências** | 155 | 28,8% | 1.77 / 5.0 | Dificuldade para localizar atalhos do Pix e travamentos durante o fluxo de envio. |
| **Design / UX** | 119 | 22,1% | 1.45 / 5.0 | Interface poluída, reestruturação de menus sem aviso prévio e tipografia inadequada. |
| **Atendimento** | 38 | 7,1% | 2.05 / 5.0 | Chatbot preso em loops infinitos e demora crítica no suporte humano. |
| **Performance** | 36 | 6,7% | 2.22 / 5.0 | Lentidão generalizada, superaquecimento do dispositivo e consumo elevado de bateria. |

---

## 🔍 Evidências Encontradas nos Dados

1. **Colapso na Porta de Entrada (Login):** 
   * *Evidência:* Mais de um terço das reclamações (35,4%) relatam barreiras para autenticação. 
   * *Exemplo de feedback:* `"O app fecha sozinho assim que coloco a digital"` / `"Erro 403 constante ao tentar entrar na conta"`.
2. **Fricção no Core Business (Transferências):** 
   * *Evidência:* A mudança de layout removeu o acesso rápido ao Pix da tela inicial, gerando 28,8% de queixas.
   * *Exemplo de feedback:* `"Cadê o botão do Pix? Tive que procurar em três menus diferentes para fazer uma transferência simples"`.
3. **Rejeição ao Novo Redesenho de Interface:** 
   * *Evidência:* 22,1% dos usuários criticam o novo fluxo visual, apontando quebra de hábito de navegação.
   * *Exemplo de feedback:* `"Mudaram tudo de lugar, ficou confuso, feio e difícil de achar a fatura do cartão"`.
4. **Paridade de Insatisfação (iOS vs. Android):** 
   * *Evidência:* A média de satisfação permanece crítica em ambas as plataformas (1.87 no iOS vs. 1.95 no Android), indicando que o problema decorre da arquitetura do *release* e não de bugs de hardware isolados.

---

## 🚀 Plano de Recomendações Práticas (Curto Prazo)

Para estancar o *churn* e recuperar a reputação nas lojas digitais, o plano de ação prioriza as seguintes frentes:

### ⚡ 1. Ações Imediatas (`Hotfix` - Próximas 48 Horas)
* **[Dev / Backend]:** Desenvolver e homologar um *patch* de emergência para corrigir o tratamento de erros na biometria e estabilizar o fluxo de inicialização do app (reduzindo os *crashes* de login).
* **[Produto]:** Implementar uma reversão parcial temporária ou injetar um atalho visual flutuante para o Pix na tela principal, restabelecendo a agilidade da principal transação do banco.

### 🛠️ 2. Ações de Curto Prazo (1ª Semana)
* **[Design / UX]:** Realizar um *tuning* rápido de interface para ajustar o contraste, aumentar tamanhos de fontes e introduzir um *onboarding* contextual (*tooltip*) guiando o usuário pelas novas posições de menus e extratos.
* **[Atendimento / IA]:** Reconfigurar o chatbot de triagem para identificar termos-chave da nova versão, direcionando os clientes afetados direto para filas prioritárias de suporte humano e atenuando a frustração.

---
*Relatório estruturado para acompanhamento via issues no GitHub.*
