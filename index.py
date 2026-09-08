<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buriti Brasa - Gestão de Pedidos e Encomendas</title>
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Supabase JS Client -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        buriti: {
                            gold: '#f59e0b',
                            goldLight: '#fde047',
                            amber: '#d97706',
                            fire: '#ea580c',
                            red: '#dc2626',
                            dark: '#0a0a0d',
                            card: '#141418',
                            border: '#27272a'
                        }
                    },
                    fontFamily: {
                        brand: ['Arial', 'Helvetica', 'sans-serif'],
                        sans: ['Arial', 'Inter', 'sans-serif']
                    }
                }
            }
        }
    </script>

    <style>
        .brand-gradient-text {
            background: linear-gradient(180deg, #fff2a8 0%, #f59e0b 55%, #b45309 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 2px 10px rgba(245, 158, 11, 0.3);
            font-family: 'Arial', sans-serif;
        }
        .brand-btn-gradient {
            background: linear-gradient(135deg, #d97706 0%, #ea580c 50%, #b91c1c 100%);
        }
        .brand-btn-gradient:hover {
            background: linear-gradient(135deg, #f59e0b 0%, #f97316 50%, #dc2626 100%);
        }
        .gold-border-glow {
            box-shadow: 0 0 20px -3px rgba(245, 158, 11, 0.25);
        }

        /* Estilos de Impressão para o Comprovante */
        @media print {
            body * {
                visibility: hidden;
            }
            #printable-receipt, #printable-receipt * {
                visibility: visible;
            }
            #printable-receipt {
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                background: #ffffff !important;
                color: #111827 !important;
                padding: 20px;
                box-shadow: none !important;
            }
            .no-print {
                display: none !important;
            }
            .print-dark-text {
                color: #111827 !important;
            }
            .print-border {
                border-color: #d1d5db !important;
            }
        }
    </style>
</head>
<body class="bg-[#09090c] text-zinc-100 font-sans min-h-screen flex flex-col antialiased">

    <!-- HEADER DA MARCA BURITI BRASA -->
    <header class="border-b border-buriti-border bg-[#101014] sticky top-0 z-30 shadow-2xl">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex flex-col md:flex-row items-center justify-between gap-4">
            
            <!-- REPRODUÇÃO DA LOGO BURITI BRASA -->
            <div class="flex items-center gap-4 cursor-pointer group" onclick="switchTab('dashboard')">
                <div class="relative flex-shrink-0 w-20 h-20 bg-black rounded-2xl p-1 shadow-xl border-2 border-amber-500/80 group-hover:scale-105 transition-transform flex flex-col items-center justify-between text-center overflow-hidden">
                    <span class="text-[7px] font-black tracking-tighter text-amber-200 uppercase font-brand mt-0.5 leading-none">ACENDEDOR DE CARVÃO</span>
                    
                    <div class="flex items-center justify-between w-full px-1 relative my-auto">
                        <!-- Palmeira Esquerda -->
                        <svg class="w-4 h-5 fill-amber-400 text-amber-400 shrink-0" viewBox="0 0 24 24"><path d="M12 2C11.5 4 10 6 7 6C6 6 5 5 5 4C3 6 3 8 5 9C7 10 9 9 10 8C9.5 11 8 13 5 14C8 14 10 12 11 10C11 13 10.5 16 9 19C10.5 18 11.5 15 12 12C12.5 15 13.5 18 15 19C13.5 16 13 13 13 10C14 12 16 14 19 14C16 13 14.5 11 14 8C15 9 17 10 19 9C21 8 21 6 19 4C19 5 18 6 17 6C14 6 12.5 4 12 2Z"/></svg>
                        
                        <div class="flex flex-col items-center leading-none px-0.5">
                            <i class="fa-solid fa-fire text-orange-500 text-[10px] animate-pulse"></i>
                            <span class="text-[13px] font-black font-brand tracking-tight text-amber-300 leading-none uppercase mt-0.5">BURITI</span>
                            <span class="text-[12px] font-black font-brand tracking-tight text-orange-400 leading-none uppercase">BRASA</span>
                            <span class="text-[5px] font-bold text-amber-200 tracking-tighter uppercase mt-0.5">ARTESANAL E SUSTENTÁVEL</span>
                        </div>
                        
                        <!-- Palmeira Direita -->
                        <svg class="w-4 h-5 fill-amber-400 text-amber-400 shrink-0 transform -scale-x-100" viewBox="0 0 24 24"><path d="M12 2C11.5 4 10 6 7 6C6 6 5 5 5 4C3 6 3 8 5 9C7 10 9 9 10 8C9.5 11 8 13 5 14C8 14 10 12 11 10C11 13 10.5 16 9 19C10.5 18 11.5 15 12 12C12.5 15 13.5 18 15 19C13.5 16 13 13 13 10C14 12 16 14 19 14C16 13 14.5 11 14 8C15 9 17 10 19 9C21 8 21 6 19 4C19 5 18 6 17 6C14 6 12.5 4 12 2Z"/></svg>
                    </div>

                    <div class="bg-amber-600/30 w-full py-0.5 text-[6px] font-extrabold text-amber-300 uppercase tracking-tighter border-t border-amber-500/40">
                        CONTÉM 4 UNIDADES
                    </div>
                </div>

                <div>
                    <span class="text-[10px] font-bold text-zinc-400 uppercase tracking-widest block font-brand">ACENDEDOR DE CARVÃO</span>
                    <h1 class="text-2xl font-black font-brand tracking-wider brand-gradient-text uppercase leading-none mt-0.5">
                        BURITI BRASA
                    </h1>
                    <p class="text-[11px] text-zinc-400 font-sans tracking-wide flex items-center gap-1.5 mt-1">
                        <span class="bg-amber-500/20 text-amber-300 text-[9px] font-extrabold px-2 py-0.5 rounded border border-amber-500/30 uppercase font-brand">
                            Artesanal e Sustentável
                        </span>
                        • <span class="text-zinc-400">São João da Ponta - PA</span>
                    </p>
                </div>
            </div>

            <!-- BOTÕES DE NAVEGAÇÃO E SUPABASE -->
            <div class="flex flex-wrap items-center gap-3">
                <button onclick="openSupabaseModal()" id="supabase-status-badge" class="bg-zinc-900 hover:bg-zinc-800 border border-zinc-700 px-3 py-1.5 rounded-xl text-xs flex items-center gap-2 transition-colors">
                    <span id="supabase-indicator" class="w-2.5 h-2.5 rounded-full bg-amber-500 animate-pulse"></span>
                    <span id="supabase-status-text" class="text-zinc-300 font-medium">Supabase: Modo Local</span>
                    <i class="fa-solid fa-gear text-zinc-500 text-xs"></i>
                </button>

                <nav class="flex items-center gap-1 bg-zinc-900/90 p-1.5 rounded-xl border border-zinc-800">
                    <button id="nav-dashboard" onclick="switchTab('dashboard')" class="px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all bg-amber-500 text-zinc-950 font-bold shadow-md">
                        <i class="fa-solid fa-chart-pie"></i>
                        <span>Painel</span>
                    </button>
                    <button id="nav-novo-pedido" onclick="switchTab('novo-pedido')" class="px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all text-zinc-300 hover:text-white hover:bg-zinc-800">
                        <i class="fa-solid fa-circle-plus text-amber-500"></i>
                        <span>Novo Pedido</span>
                    </button>
                    <button id="nav-pedidos" onclick="switchTab('pedidos')" class="px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all text-zinc-300 hover:text-white hover:bg-zinc-800 relative">
                        <i class="fa-solid fa-boxes-packing"></i>
                        <span>Encomendas</span>
                        <span id="badge-total-pedidos" class="bg-orange-600 text-white text-[10px] px-1.5 py-0.2 rounded-full font-bold ml-1">0</span>
                    </button>
                </nav>
            </div>

        </div>
    </header>

    <!-- CONTEÚDO PRINCIPAL -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">

        <!-- TAB 1: PAINEL / DASHBOARD -->
        <section id="tab-dashboard" class="space-y-6">
            <div class="relative rounded-2xl bg-gradient-to-r from-zinc-900 via-[#1c1510] to-zinc-900 border border-amber-500/30 p-6 md:p-8 overflow-hidden shadow-2xl gold-border-glow">
                <div class="absolute -right-6 -bottom-10 opacity-10 text-amber-500 text-9xl pointer-events-none">
                    <i class="fa-solid fa-fire"></i>
                </div>
                <div class="relative z-10 max-w-3xl">
                    <div class="flex items-center gap-2 mb-2">
                        <span class="text-amber-400 font-bold text-xs uppercase tracking-widest bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/30 flex items-center gap-1.5">
                            <i class="fa-solid fa-box text-orange-400"></i> Caixas Contêm 4 Unidades • 10 Minutos de Chama
                        </span>
                    </div>
                    <h2 class="text-2xl md:text-3xl font-black font-brand text-white mt-1 uppercase">
                        Gestão Oficial de Vendas & Encomendas
                    </h2>
                    <p class="text-zinc-300 text-xs md:text-sm mt-2 leading-relaxed">
                        Preencha a ficha oficial com o nome do estabelecimento, CNPJ, endereço e quantidade de dúzias/cartelas do <strong class="text-amber-400">Acendedor Buriti Brasa</strong>.
                    </p>

                    <div class="mt-5 flex flex-wrap gap-3">
                        <button onclick="switchTab('novo-pedido')" class="brand-btn-gradient text-white text-xs font-extrabold px-5 py-2.5 rounded-xl shadow-lg flex items-center gap-2 transform active:scale-95 transition-transform">
                            <i class="fa-solid fa-plus-circle"></i>
                            Preencher Nova Ficha de Encomenda
                        </button>
                        <button onclick="openSupabaseModal()" class="bg-zinc-800 hover:bg-zinc-700 text-zinc-200 text-xs font-semibold px-4 py-2.5 rounded-xl border border-zinc-700 flex items-center gap-2">
                            <i class="fa-solid fa-database text-amber-400"></i>
                            Conectar Banco Supabase
                        </button>
                    </div>
                </div>
            </div>

            <!-- CARDS DE MÉTRICAS -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="bg-buriti-card border border-buriti-border rounded-xl p-5 shadow-lg relative">
                    <div class="flex justify-between items-start">
                        <div>
                            <p class="text-xs font-semibold text-zinc-400 uppercase tracking-wider">Total de Pedidos</p>
                            <h3 id="stat-total-pedidos" class="text-2xl font-black text-white mt-1">0</h3>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400 flex items-center justify-center">
                            <i class="fa-solid fa-receipt text-lg"></i>
                        </div>
                    </div>
                    <p class="text-[11px] text-zinc-500 mt-3 flex items-center gap-1">
                        <i class="fa-solid fa-folder-open text-amber-500"></i> Fichas registradas
                    </p>
                </div>

                <div class="bg-buriti-card border border-buriti-border rounded-xl p-5 shadow-lg relative">
                    <div class="flex justify-between items-start">
                        <div>
                            <p class="text-xs font-semibold text-zinc-400 uppercase tracking-wider">Volume de Dúzias</p>
                            <h3 id="stat-total-duzias" class="text-2xl font-black text-amber-400 mt-1">0 dz</h3>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-orange-500/10 border border-orange-500/20 text-orange-400 flex items-center justify-center">
                            <i class="fa-solid fa-boxes-stacked text-lg"></i>
                        </div>
                    </div>
                    <p class="text-[11px] text-zinc-500 mt-3 flex items-center gap-1">
                        <i class="fa-solid fa-box text-orange-500"></i> Cartelas encomendadas
                    </p>
                </div>

                <div class="bg-buriti-card border border-buriti-border rounded-xl p-5 shadow-lg relative">
                    <div class="flex justify-between items-start">
                        <div>
                            <p class="text-xs font-semibold text-zinc-400 uppercase tracking-wider">Faturamento Total</p>
                            <h3 id="stat-total-faturamento" class="text-2xl font-black text-emerald-400 mt-1">R$ 0,00</h3>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-center">
                            <i class="fa-solid fa-hand-holding-dollar text-lg"></i>
                        </div>
                    </div>
                    <p class="text-[11px] text-zinc-500 mt-3 flex items-center gap-1">
                        <i class="fa-solid fa-circle-check text-emerald-500"></i> Em vendas brutas
                    </p>
                </div>

                <div class="bg-buriti-card border border-buriti-border rounded-xl p-5 shadow-lg relative">
                    <div class="flex justify-between items-start">
                        <div>
                            <p class="text-xs font-semibold text-zinc-400 uppercase tracking-wider">Pendentes de Entrega</p>
                            <h3 id="stat-pedidos-pendentes" class="text-2xl font-black text-amber-300 mt-1">0</h3>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-red-500/10 border border-red-500/20 text-red-400 flex items-center justify-center">
                            <i class="fa-solid fa-truck-ramp-box text-lg"></i>
                        </div>
                    </div>
                    <p class="text-[11px] text-zinc-500 mt-3 flex items-center gap-1">
                        <i class="fa-solid fa-clock text-amber-500"></i> Aguardando envio
                    </p>
                </div>
            </div>

            <div class="bg-buriti-card border border-buriti-border rounded-2xl p-5 shadow-xl">
                <div class="flex items-center justify-between mb-4">
                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-clock-rotate-left text-amber-500"></i>
                        <h3 class="font-bold text-white text-sm uppercase tracking-wider font-brand">Últimas Encomendas Gravadas</h3>
                    </div>
                    <button onclick="switchTab('pedidos')" class="text-xs text-amber-400 hover:text-amber-300 font-semibold flex items-center gap-1">
                        Ver todas <i class="fa-solid fa-arrow-right text-[10px]"></i>
                    </button>
                </div>
                <div id="recent-orders-list" class="space-y-3"></div>
            </div>
        </section>

        <!-- TAB 2: FICHA / FORMULÁRIO PREENCHÍVEL DE NOVO PEDIDO -->
        <section id="tab-novo-pedido" class="hidden space-y-6">
            <div class="bg-buriti-card border border-buriti-border rounded-2xl p-6 md:p-8 shadow-2xl max-w-4xl mx-auto gold-border-glow">
                
                <div class="border-b border-zinc-800 pb-5 mb-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                    <div class="flex items-center gap-4">
                        <div class="w-16 h-16 bg-black rounded-xl p-1 border-2 border-amber-500/80 flex flex-col items-center justify-between text-center shrink-0">
                            <span class="text-[6px] font-black text-amber-200 font-brand uppercase tracking-tighter">ACENDEDOR DE CARVÃO</span>
                            <div class="flex items-center justify-center gap-0.5 my-auto">
                                <svg class="w-3 h-3 fill-amber-400" viewBox="0 0 24 24"><path d="M12 2C11.5 4 10 6 7 6C6 6 5 5 5 4C3 6 3 8 5 9C7 10 9 9 10 8C9.5 11 8 13 5 14C8 14 10 12 11 10C11 13 10.5 16 9 19C10.5 18 11.5 15 12 12C12.5 15 13.5 18 15 19C13.5 16 13 13 13 10C14 12 16 14 19 14C16 13 14.5 11 14 8C15 9 17 10 19 9C21 8 21 6 19 4C19 5 18 6 17 6C14 6 12.5 4 12 2Z"/></svg>
                                <div class="text-center leading-none">
                                    <span class="text-[10px] font-black text-amber-300 font-brand block">BURITI</span>
                                    <span class="text-[9px] font-black text-orange-400 font-brand block">BRASA</span>
                                </div>
                                <svg class="w-3 h-3 fill-amber-400 transform -scale-x-100" viewBox="0 0 24 24"><path d="M12 2C11.5 4 10 6 7 6C6 6 5 5 5 4C3 6 3 8 5 9C7 10 9 9 10 8C9.5 11 8 13 5 14C8 14 10 12 11 10C11 13 10.5 16 9 19C10.5 18 11.5 15 12 12C12.5 15 13.5 18 15 19C13.5 16 13 13 13 10C14 12 16 14 19 14C16 13 14.5 11 14 8C15 9 17 10 19 9C21 8 21 6 19 4C19 5 18 6 17 6C14 6 12.5 4 12 2Z"/></svg>
                            </div>
                            <span class="text-[5px] font-bold text-amber-200 uppercase tracking-tighter">CONTÉM 4 UNIDADES</span>
                        </div>
                        <div>
                            <h2 class="text-xl font-black text-white font-brand uppercase tracking-wide">
                                Ficha de Registro de Encomenda
                            </h2>
                            <p class="text-xs text-amber-400 font-bold font-brand uppercase">
                                Acendedor de Carvão Buriti Brasa • Artesanal e Sustentável
                            </p>
                        </div>
                    </div>

                    <div class="bg-zinc-900 border border-amber-500/30 px-3.5 py-1.5 rounded-xl text-right">
                        <span class="text-[10px] text-zinc-400 block uppercase font-bold tracking-wider font-brand">Número da Ficha</span>
                        <span id="form-order-number" class="text-sm font-black text-amber-400 font-mono">#BB-2026-001</span>
                    </div>
                </div>

                <form id="order-form" onsubmit="handleSaveOrder(event)" class="space-y-6">
                    <!-- DADOS DO CLIENTE -->
                    <div class="space-y-4">
                        <h3 class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2 font-brand">
                            <i class="fa-solid fa-store"></i> 1. Dados do Estabelecimento & Cliente
                        </h3>
                        
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <label class="block text-xs font-semibold text-zinc-300 mb-1">Nome do Estabelecimento / Razão Social *</label>
                                <input type="text" id="client_name" required placeholder="Ex: Supermercado Carajás" class="w-full bg-zinc-900 border border-zinc-700 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-amber-500">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-zinc-300 mb-1">Nome Fantasia (Se houver)</label>
                                <input type="text" id="client_trade_name" placeholder="Ex: Mercadinho da Praça" class="w-full bg-zinc-900 border border-zinc-700 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-amber-500">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-zinc-300 mb-1">CNPJ ou CPF *</label>
                                <input type="text" id="client_doc" required placeholder="00.000.000/0001-00" class="w-full bg-zinc-900 border border-zinc-700 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-amber-500">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-zinc-300 mb-1">Telefone / WhatsApp *</label>
                                <input type="text" id="client_phone" required placeholder="(91) 98000-0000" class="w-full bg-zinc-900 border border-zinc-700 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-amber-500">
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                            <div class="md:col-span-2">
                                <label class="block text-xs font-semibold text-zinc-300 mb-1">Endereço de Entrega Completo *</label>
                                <input type="text" id="client_address" required placeholder="Av. Principal, nº 123 - Centro" class="w-full bg-zinc-900 border border-zinc-700 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-amber-500">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-zinc-300 mb-1">Cidade / UF *</label>
                                <input type="text" id="client_city" required placeholder="São João da Ponta/PA" class="w-full bg-zinc-900 border border-zinc-700 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-amber-500">
                            </div>
                        </div>
                    </div>

                    <!-- QUANTIDADES -->
                    <div class="space-y-4 pt-4 border-t border-zinc-800">
                        <h3 class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2 font-brand">
                            <i class="fa-solid fa-boxes-packing"></i> 2. Quantidade de Dúzias e Cartelas (Caixas de 4 Unid.)
                        </h3>

                        <div class="bg-zinc-900/80 border border-zinc-800 rounded-xl p-4 space-y-4">
                            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 items-center">
                                <div>
                                    <label class="block text-xs font-semibold text-zinc-300 mb-1">Qtd. de Dúzias (1 dz = 12 cartelas)</label>
                                    <div class="relative">
                                        <input type="number" id="qty_dozens" min="0" step="0.5" value="1" oninput="calculateTotals()" class="w-full bg-zinc-950 border border-amber-500/50 rounded-xl px-3.5 py-2.5 text-sm font-bold text-amber-400 focus:outline-none focus:border-amber-500">
                                        <span class="absolute right-3 top-2.5 text-xs text-zinc-500 font-semibold">Dúzias</span>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-xs font-semibold text-zinc-300 mb-1">+ Cartelas Soltas (Avulsas)</label>
                                    <div class="relative">
                                        <input type="number" id="qty_units" min="0" value="0" oninput="calculateTotals()" class="w-full bg-zinc-950 border border-zinc-700 rounded-xl px-3.5 py-2.5 text-sm text-white focus:outline-none focus:border-amber-500">
                                        <span class="absolute right-3 top-2.5 text-xs text-zinc-500 font-semibold">Cartelas</span>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-xs font-semibold text-zinc-300 mb-1">Preço por Dúzia (R$) *</label>
                                    <div class="relative">
                                        <span class="absolute left-3 top-2.5 text-xs text-zinc-400 font-bold">R$</span>
                                        <input type="number" id="price_per_dozen" min="0" step="0.50" value="60.00" oninput="calculateTotals()" class="w-full bg-zinc-950 border border-zinc-700 rounded-xl pl-8 pr-3.5 py-2.5 text-sm text-emerald-400 font-bold focus:outline-none focus:border-amber-500">
                                    </div>
                                </div>
                            </div>

                            <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-3 flex flex-wrap items-center justify-between text-xs text-amber-300 gap-2">
                                <div class="flex items-center gap-2">
                                    <i class="fa-solid fa-circle-info text-amber-400 text-sm"></i>
                                    <span>
                                        Total de Cartelas: <strong id="calc-total-cartelas" class="text-white font-bold">12</strong> caixas
                                        <span class="text-zinc-400"> (equivale a <span id="calc-total-acendedores" class="text-amber-400 font-bold">48</span> acendedores/cones de queima)</span>
                                    </span>
                                </div>
                                <div class="text-sm font-black text-emerald-400 font-mono">
                                    Subtotal: R$ <span id="calc-subtotal-val">60,00</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- PAGAMENTO E ENTREGA -->
                    <div class="space-y-4 pt-4 border-t border-zinc-800">
                        <h3 class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2 font-brand">
                            <i class="fa-solid fa-truck-fast"></i> 3. Condições de Pagamento e Prazo de Entrega
                        </h3>

                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                            <div>
                                <label class="block text-xs font-semibold text-zinc-300 mb-1">Forma de Pagamento</label>
                                <select id="payment_method" class="w-full bg-zinc-900 border border-zinc-700 rounded-xl px-3.5 py-2.5 text-xs text-white focus:outline-none focus:border-amber-500">
                                    <option value="PIX / Transferência">PIX / Transferência</option>
                                    <option value="Dinheiro na Entrega">Dinheiro na Entrega</option>
                                    <option value="Boleto 14 dias">Boleto (14 Dias)</option>
                                    <option value="Cartão de Crédito">Cartão de Crédito</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-zinc-300 mb-1">Data do Pedido</label>
                                <input type="date" id="order_date" required class="w-full bg-zinc-900 border border-zinc-700 rounded-xl px-3.5 py-2.5 text-xs text-white focus:outline-none">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-zinc-300 mb-1">Previsão de Entrega</label>
                                <input type="date" id="delivery_date" required class="w-full bg-zinc-900 border border-zinc-700 rounded-xl px-3.5 py-2.5 text-xs text-white focus:outline-none">
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-zinc-300 mb-1">Observações / Instruções de Entrega</label>
                            <textarea id="order_notes" rows="2" placeholder="Ex: Entregar pela manhã no depósito principal." class="w-full bg-zinc-900 border border-zinc-700 rounded-xl px-3.5 py-2 text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-amber-500"></textarea>
                        </div>
                    </div>

                    <div class="bg-zinc-900 border border-zinc-800 rounded-xl p-4 flex flex-col sm:flex-row items-center justify-between gap-4">
                        <div>
                            <span class="text-xs text-zinc-400 block font-medium">VALOR TOTAL DO PEDIDO</span>
                            <div class="text-2xl font-black text-emerald-400 font-mono">
                                R$ <span id="calc-final-total">60,00</span>
                            </div>
                        </div>

                        <div class="flex items-center gap-3 w-full sm:w-auto">
                            <button type="button" onclick="resetForm()" class="px-4 py-2.5 rounded-xl border border-zinc-700 text-zinc-300 text-xs font-semibold hover:bg-zinc-800 w-1/2 sm:w-auto">
                                Limpar
                            </button>
                            <button type="submit" id="btn-save-order" class="brand-btn-gradient text-white text-xs font-bold px-6 py-2.5 rounded-xl shadow-lg flex items-center justify-center gap-2 w-1/2 sm:w-auto">
                                <i class="fa-solid fa-floppy-disk"></i>
                                Salvar Encomenda
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </section>

        <!-- TAB 3: LISTA DE PEDIDOS / ENCOMENDAS -->
        <section id="tab-pedidos" class="hidden space-y-6">
            <div class="bg-buriti-card border border-buriti-border rounded-2xl p-6 shadow-xl space-y-4">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-zinc-800 pb-4">
                    <div>
                        <h2 class="text-lg font-bold text-white font-brand flex items-center gap-2 uppercase tracking-wide">
                            <i class="fa-solid fa-boxes-packing text-amber-500"></i>
                            Encomendas Gravadas
                        </h2>
                        <p class="text-xs text-zinc-400">Histórico de pedidos salvos no sistema</p>
                    </div>

                    <div class="flex flex-col sm:flex-row items-center gap-3">
                        <div class="relative w-full sm:w-64">
                            <i class="fa-solid fa-magnifying-glass absolute left-3 top-2.5 text-xs text-zinc-500"></i>
                            <input type="text" id="search-input" oninput="renderOrdersTable()" placeholder="Buscar cliente ou CNPJ..." class="w-full bg-zinc-900 border border-zinc-700 rounded-xl pl-9 pr-3 py-2 text-xs text-white placeholder-zinc-500 focus:outline-none">
                        </div>

                        <select id="status-filter" onchange="renderOrdersTable()" class="w-full sm:w-auto bg-zinc-900 border border-zinc-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none">
                            <option value="TODOS">Todos os Status</option>
                            <option value="Pendente">Pendente</option>
                            <option value="Em Produção">Em Produção</option>
                            <option value="A Caminho">A Caminho</option>
                            <option value="Entregue">Entregue</option>
                        </select>
                    </div>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs">
                        <thead class="bg-zinc-900/80 text-zinc-400 uppercase font-semibold border-b border-zinc-800 font-brand">
                            <tr>
                                <th class="px-4 py-3">Ficha Nº</th>
                                <th class="px-4 py-3">Cliente / CNPJ</th>
                                <th class="px-4 py-3">Volume (Dúzias)</th>
                                <th class="px-4 py-3">Valor Total</th>
                                <th class="px-4 py-3">Entrega</th>
                                <th class="px-4 py-3">Status</th>
                                <th class="px-4 py-3 text-right">Ações</th>
                            </tr>
                        </thead>
                        <tbody id="orders-table-body" class="divide-y divide-zinc-800 text-zinc-300"></tbody>
                    </table>
                </div>

                <div id="no-orders-msg" class="hidden text-center py-8 text-zinc-500 text-xs">
                    <i class="fa-solid fa-box-open text-3xl mb-2 text-zinc-600 block"></i>
                    Nenhuma encomenda encontrada.
                </div>
            </div>
        </section>

    </main>

    <!-- MODAL SUPABASE -->
    <div id="supabase-modal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
        <div class="bg-zinc-900 border border-amber-500/40 rounded-2xl max-w-lg w-full p-6 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-zinc-800 pb-3">
                <h3 class="font-bold text-white text-base flex items-center gap-2 font-brand">
                    <i class="fa-solid fa-database text-amber-500"></i>
                    Conexão com Banco Supabase
                </h3>
                <button onclick="closeSupabaseModal()" class="text-zinc-400 hover:text-white">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <p class="text-xs text-zinc-300 leading-relaxed">
                Insira suas credenciais do projeto Supabase. Os pedidos salvos serão sincronizados na nuvem!
            </p>

            <div class="space-y-3">
                <div>
                    <label class="block text-xs font-semibold text-zinc-300 mb-1">Supabase Project URL</label>
                    <input type="text" id="supabase-url" placeholder="https://xyzcompany.supabase.co" class="w-full bg-zinc-950 border border-zinc-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none font-mono">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-zinc-300 mb-1">Supabase Anon Key (Public Key)</label>
                    <input type="text" id="supabase-key" placeholder="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." class="w-full bg-zinc-950 border border-zinc-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none font-mono">
                </div>
            </div>

            <div class="flex items-center justify-end gap-2 pt-2">
                <button onclick="clearSupabaseConfig()" class="px-3 py-2 rounded-xl text-xs font-semibold text-red-400 hover:bg-zinc-800">
                    Desconectar
                </button>
                <button onclick="saveSupabaseConfig()" class="brand-btn-gradient text-white text-xs font-bold px-5 py-2 rounded-xl">
                    Salvar e Conectar
                </button>
            </div>
        </div>
    </div>

    <!-- MODAL IMPRESSÃO COMPROVANTE -->
    <div id="receipt-modal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
        <div class="bg-zinc-900 border border-amber-500/40 rounded-2xl max-w-2xl w-full max-h-[92vh] overflow-y-auto shadow-2xl flex flex-col">
            <div class="no-print p-4 border-b border-zinc-800 flex items-center justify-between bg-zinc-950">
                <span class="text-xs font-bold text-amber-400 flex items-center gap-2 font-brand">
                    <i class="fa-solid fa-print"></i> Visualização para Impressão
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="window.print()" class="bg-amber-500 hover:bg-amber-400 text-zinc-950 font-bold text-xs px-3 py-1.5 rounded-lg flex items-center gap-1 font-brand">
                        <i class="fa-solid fa-print"></i> Imprimir / PDF
                    </button>
                    <button onclick="closeModal()" class="text-zinc-400 hover:text-white px-2 py-1">
                        <i class="fa-solid fa-xmark text-lg"></i>
                    </button>
                </div>
            </div>

            <div id="printable-receipt" class="p-8 bg-white text-zinc-900">
                <div class="border-b-2 border-amber-600 pb-4 mb-5 flex items-center justify-between">
                    <div class="flex items-center gap-4">
                        <div class="w-16 h-16 bg-black rounded-xl p-1 border-2 border-amber-600 flex flex-col items-center justify-between text-center shrink-0">
                            <span class="text-[6px] font-black text-amber-300 font-brand uppercase tracking-tighter">ACENDEDOR DE CARVÃO</span>
                            <div class="flex items-center justify-center gap-0.5 my-auto">
                                <svg class="w-3 h-3 fill-amber-400" viewBox="0 0 24 24"><path d="M12 2C11.5 4 10 6 7 6C6 6 5 5 5 4C3 6 3 8 5 9C7 10 9 9 10 8C9.5 11 8 13 5 14C8 14 10 12 11 10C11 13 10.5 16 9 19C10.5 18 11.5 15 12 12C12.5 15 13.5 18 15 19C13.5 16 13 13 13 10C14 12 16 14 19 14C16 13 14.5 11 14 8C15 9 17 10 19 9C21 8 21 6 19 4C19 5 18 6 17 6C14 6 12.5 4 12 2Z"/></svg>
                                <div class="text-center leading-none">
                                    <span class="text-[10px] font-black text-amber-400 font-brand block">BURITI</span>
                                    <span class="text-[9px] font-black text-orange-400 font-brand block">BRASA</span>
                                </div>
                                <svg class="w-3 h-3 fill-amber-400 transform -scale-x-100" viewBox="0 0 24 24"><path d="M12 2C11.5 4 10 6 7 6C6 6 5 5 5 4C3 6 3 8 5 9C7 10 9 9 10 8C9.5 11 8 13 5 14C8 14 10 12 11 10C11 13 10.5 16 9 19C10.5 18 11.5 15 12 12C12.5 15 13.5 18 15 19C13.5 16 13 13 13 10C14 12 16 14 19 14C16 13 14.5 11 14 8C15 9 17 10 19 9C21 8 21 6 19 4C19 5 18 6 17 6C14 6 12.5 4 12 2Z"/></svg>
                            </div>
                            <span class="text-[5px] font-bold text-white uppercase tracking-tighter">CONTÉM 4 UNIDADES</span>
                        </div>
                        <div>
                            <span class="text-[10px] font-bold text-amber-700 font-brand uppercase tracking-widest block">ACENDEDOR DE CARVÃO</span>
                            <h1 class="text-2xl font-black font-brand text-zinc-900 tracking-wider uppercase print-dark-text leading-none">
                                BURITI BRASA
                            </h1>
                            <p class="text-xs font-bold text-amber-800 uppercase tracking-wide mt-1 font-brand">
                                ARTESANAL E SUSTENTÁVEL
                            </p>
                            <p class="text-[11px] text-zinc-600">
                                Fabricado em São João da Ponta - Pará • Caixa com 4 unidades
                            </p>
                        </div>
                    </div>
                    <div class="text-right">
                        <span class="text-xs font-bold text-zinc-500 block uppercase font-brand">Ficha de Pedido</span>
                        <span id="rec-order-id" class="text-base font-black text-amber-700 font-mono">#BB-000</span>
                        <span id="rec-date" class="text-[11px] text-zinc-500 block">00/00/2026</span>
                    </div>
                </div>

                <div class="bg-zinc-50 border border-zinc-300 rounded-lg p-4 mb-5 text-xs space-y-1.5 print-border">
                    <h3 class="font-bold text-zinc-900 uppercase tracking-wider text-[11px] border-b border-zinc-200 pb-1 mb-2 font-brand">
                        Dados do Estabelecimento / Cliente
                    </h3>
                    <div class="grid grid-cols-2 gap-2">
                        <p><strong class="text-zinc-700">Razão Social:</strong> <span id="rec-client-name">-</span></p>
                        <p><strong class="text-zinc-700">Nome Fantasia:</strong> <span id="rec-trade-name">-</span></p>
                        <p><strong class="text-zinc-700">CNPJ / CPF:</strong> <span id="rec-client-doc">-</span></p>
                        <p><strong class="text-zinc-700">Telefone / Fone:</strong> <span id="rec-client-phone">-</span></p>
                        <p class="col-span-2"><strong class="text-zinc-700">Endereço de Entrega:</strong> <span id="rec-client-address">-</span></p>
                        <p class="col-span-2"><strong class="text-zinc-700">Cidade / UF:</strong> <span id="rec-client-city">-</span></p>
                    </div>
                </div>

                <table class="w-full text-xs text-left mb-6 border-collapse">
                    <thead>
                        <tr class="bg-amber-100 border-y border-amber-600 text-amber-950 font-bold uppercase font-brand">
                            <th class="py-2 px-3">Descrição do Produto</th>
                            <th class="py-2 px-3 text-center">Dúzias</th>
                            <th class="py-2 px-3 text-center">Cartelas</th>
                            <th class="py-2 px-3 text-right">Preço Dúzia</th>
                            <th class="py-2 px-3 text-right">Subtotal</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-zinc-300 text-zinc-900">
                        <tr>
                            <td class="py-3 px-3">
                                <strong>Acendedor Buriti Brasa (4 Unidades)</strong><br>
                                <span class="text-[10px] text-zinc-600">Sem cheiro químico • 10 minutos de chama</span>
                            </td>
                            <td id="rec-qty-dozens" class="py-3 px-3 text-center font-bold">0 dz</td>
                            <td id="rec-qty-cartelas" class="py-3 px-3 text-center">0 un.</td>
                            <td id="rec-price-dozen" class="py-3 px-3 text-right">R$ 0,00</td>
                            <td id="rec-subtotal" class="py-3 px-3 text-right font-bold">R$ 0,00</td>
                        </tr>
                    </tbody>
                </table>

                <div class="flex justify-between items-start mb-8 text-xs">
                    <div class="space-y-1">
                        <p><strong class="text-zinc-700">Pagamento:</strong> <span id="rec-payment">-</span></p>
                        <p><strong class="text-zinc-700">Previsão de Entrega:</strong> <span id="rec-delivery-date">-</span></p>
                        <p><strong class="text-zinc-700">Status:</strong> <span id="rec-status" class="font-bold">-</span></p>
                        <div class="mt-2 text-[10px] text-zinc-600 italic max-w-xs" id="rec-notes-container">
                            Obs: <span id="rec-notes">Nenhuma instrução adicional.</span>
                        </div>
                    </div>

                    <div class="bg-amber-50 border-2 border-amber-500 rounded-lg p-3 text-right min-w-[180px]">
                        <span class="text-[10px] font-bold text-amber-900 uppercase block font-brand">VALOR TOTAL DO PEDIDO</span>
                        <span id="rec-final-total" class="text-2xl font-black text-amber-800 font-mono">R$ 0,00</span>
                    </div>
                </div>

                <div class="pt-10 border-t border-zinc-300 grid grid-cols-2 gap-8 text-center text-xs text-zinc-700">
                    <div>
                        <div class="border-b border-zinc-400 mb-1"></div>
                        <p class="font-bold font-brand">Buriti Brasa - Vendas</p>
                    </div>
                    <div>
                        <div class="border-b border-zinc-400 mb-1"></div>
                        <p class="font-bold font-brand">Assinatura do Cliente / Recebedor</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        let orders = [];
        let supabaseClient = null;

        const defaultOrders = [
            {
                id: "BB-2026-001",
                client_name: "Supermercado Tapajós",
                client_trade_name: "Tapajós Centro",
                client_doc: "12.345.678/0001-90",
                client_phone: "(91) 98112-3344",
                client_address: "Av. Barão do Rio Branco, 450",
                client_city: "São João da Ponta/PA",
                qty_dozens: 5,
                qty_units: 0,
                price_per_dozen: 60.00,
                payment_method: "PIX / Transferência",
                order_date: "2026-09-01",
                delivery_date: "2026-09-05",
                order_notes: "Entregar no setor de cargas.",
                status: "Entregue"
            }
        ];

        window.onload = function() {
            initSupabaseFromStorage();
            const today = new Date().toISOString().split('T')[0];
            document.getElementById('order_date').value = today;
            document.getElementById('delivery_date').value = today;

            fetchOrders();
            generateNewOrderId();
            calculateTotals();
        };

        function initSupabaseFromStorage() {
            const url = localStorage.getItem('buriti_supabase_url');
            const key = localStorage.getItem('buriti_supabase_key');

            if (url && key && window.supabase) {
                try {
                    supabaseClient = window.supabase.createClient(url, key);
                    document.getElementById('supabase-indicator').className = "w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse";
                    document.getElementById('supabase-status-text').textContent = "Supabase: Conectado";
                    document.getElementById('supabase-url').value = url;
                    document.getElementById('supabase-key').value = key;
                } catch(e) {
                    console.error("Erro ao inicializar Supabase:", e);
                }
            } else {
                document.getElementById('supabase-indicator').className = "w-2.5 h-2.5 rounded-full bg-amber-500";
                document.getElementById('supabase-status-text').textContent = "Supabase: Modo Local";
            }
        }

        async function fetchOrders() {
            if (supabaseClient) {
                try {
                    const { data, error } = await supabaseClient
                        .from('pedidos')
                        .select('*')
                        .order('created_at', { ascending: false });

                    if (!error && data) {
                        orders = data;
                        updateDashboard();
                        renderOrdersTable();
                        return;
                    }
                } catch(err) {
                    console.warn("Falha ao consultar Supabase, alternando para LocalStorage", err);
                }
            }

            const saved = localStorage.getItem('buriti_brasa_orders');
            if (saved) {
                try { orders = JSON.parse(saved); } catch(e) { orders = defaultOrders; }
            } else {
                orders = defaultOrders;
                localStorage.setItem('buriti_brasa_orders', JSON.stringify(orders));
            }
            updateDashboard();
            renderOrdersTable();
        }

        async function saveOrderData(orderObj) {
            if (supabaseClient) {
                try {
                    const { error } = await supabaseClient.from('pedidos').insert([orderObj]);
                    if (error) {
                        console.error("Erro Supabase:", error);
                        alert("Salvo localmente. Não foi possível conectar ao Supabase: " + error.message);
                    }
                } catch(err) { console.error(err); }
            }

            orders.unshift(orderObj);
            localStorage.setItem('buriti_brasa_orders', JSON.stringify(orders));
            updateDashboard();
            renderOrdersTable();
        }

        function switchTab(tabName) {
            document.getElementById('tab-dashboard').classList.add('hidden');
            document.getElementById('tab-novo-pedido').classList.add('hidden');
            document.getElementById('tab-pedidos').classList.add('hidden');

            document.getElementById('nav-dashboard').className = "px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all text-zinc-300 hover:text-white hover:bg-zinc-800";
            document.getElementById('nav-novo-pedido').className = "px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all text-zinc-300 hover:text-white hover:bg-zinc-800";
            document.getElementById('nav-pedidos').className = "px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all text-zinc-300 hover:text-white hover:bg-zinc-800 relative";

            if (tabName === 'dashboard') {
                document.getElementById('tab-dashboard').classList.remove('hidden');
                document.getElementById('nav-dashboard').className = "px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all bg-amber-500 text-zinc-950 font-bold shadow-md";
                updateDashboard();
            } else if (tabName === 'novo-pedido') {
                document.getElementById('tab-novo-pedido').classList.remove('hidden');
                document.getElementById('nav-novo-pedido').className = "px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all bg-amber-500 text-zinc-950 font-bold shadow-md";
            } else if (tabName === 'pedidos') {
                document.getElementById('tab-pedidos').classList.remove('hidden');
                document.getElementById('nav-pedidos').className = "px-3.5 py-2 rounded-lg text-xs font-semibold flex items-center gap-2 transition-all bg-amber-500 text-zinc-950 font-bold shadow-md";
                renderOrdersTable();
            }
        }

        function generateNewOrderId() {
            const strNum = String(orders.length + 1).padStart(3, '0');
            const newId = `#BB-2026-${strNum}`;
            document.getElementById('form-order-number').textContent = newId;
            return newId;
        }

        function calculateTotals() {
            const dozens = parseFloat(document.getElementById('qty_dozens').value) || 0;
            const avulsas = parseInt(document.getElementById('qty_units').value) || 0;
            const pricePerDozen = parseFloat(document.getElementById('price_per_dozen').value) || 0;

            const totalCartelas = (dozens * 12) + avulsas;
            const totalAcendedores = totalCartelas * 4;
            const totalValue = (dozens * pricePerDozen) + (avulsas * (pricePerDozen / 12));

            document.getElementById('calc-total-cartelas').textContent = totalCartelas;
            document.getElementById('calc-total-acendedores').textContent = totalAcendedores;
            document.getElementById('calc-subtotal-val').textContent = totalValue.toFixed(2).replace('.', ',');
            document.getElementById('calc-final-total').textContent = totalValue.toFixed(2).replace('.', ',');
        }

        async function handleSaveOrder(e) {
            e.preventDefault();

            const dozens = parseFloat(document.getElementById('qty_dozens').value) || 0;
            const avulsas = parseInt(document.getElementById('qty_units').value) || 0;
            const pricePerDozen = parseFloat(document.getElementById('price_per_dozen').value) || 0;

            const newOrder = {
                id: document.getElementById('form-order-number').textContent,
                client_name: document.getElementById('client_name').value,
                client_trade_name: document.getElementById('client_trade_name').value,
                client_doc: document.getElementById('client_doc').value,
                client_phone: document.getElementById('client_phone').value,
                client_address: document.getElementById('client_address').value,
                client_city: document.getElementById('client_city').value,
                qty_dozens: dozens,
                qty_units: avulsas,
                price_per_dozen: pricePerDozen,
                payment_method: document.getElementById('payment_method').value,
                order_date: document.getElementById('order_date').value,
                delivery_date: document.getElementById('delivery_date').value,
                order_notes: document.getElementById('order_notes').value,
                status: "Pendente"
            };

            await saveOrderData(newOrder);
            openReceiptModal(newOrder.id);
            resetForm();
            switchTab('pedidos');
        }

        function resetForm() {
            document.getElementById('order-form').reset();
            document.getElementById('qty_dozens').value = 1;
            document.getElementById('qty_units').value = 0;
            document.getElementById('price_per_dozen').value = "60.00";
            const today = new Date().toISOString().split('T')[0];
            document.getElementById('order_date').value = today;
            document.getElementById('delivery_date').value = today;
            generateNewOrderId();
            calculateTotals();
        }

        function updateDashboard() {
            document.getElementById('stat-total-pedidos').textContent = orders.length;
            document.getElementById('badge-total-pedidos').textContent = orders.length;

            let totalDozens = 0, totalRevenue = 0, pendingCount = 0;

            orders.forEach(o => {
                const dz = parseFloat(o.qty_dozens) || 0;
                const un = parseFloat(o.qty_units) || 0;
                const pr = parseFloat(o.price_per_dozen) || 0;

                totalDozens += dz + (un / 12);
                totalRevenue += (dz * pr) + (un * (pr / 12));
                if (o.status === 'Pendente' || o.status === 'Em Produção') pendingCount++;
            });

            document.getElementById('stat-total-duzias').textContent = totalDozens.toFixed(1) + " dz";
            document.getElementById('stat-total-faturamento').textContent = "R$ " + totalRevenue.toLocaleString('pt-BR', { minimumFractionDigits: 2 });
            document.getElementById('stat-pedidos-pendentes').textContent = pendingCount;

            const recentContainer = document.getElementById('recent-orders-list');
            if (orders.length === 0) {
                recentContainer.innerHTML = '<p class="text-xs text-zinc-500 py-4 text-center">Nenhuma encomenda cadastrada até o momento.</p>';
                return;
            }

            recentContainer.innerHTML = orders.slice(0, 4).map(o => {
                const dz = parseFloat(o.qty_dozens) || 0;
                const un = parseFloat(o.qty_units) || 0;
                const pr = parseFloat(o.price_per_dozen) || 0;
                const totalVal = (dz * pr) + (un * (pr / 12));

                return `
                    <div class="bg-zinc-900/90 border border-zinc-800 rounded-xl p-3 flex flex-wrap items-center justify-between gap-3 hover:border-amber-500/40 transition-colors">
                        <div class="flex items-center gap-3">
                            <div class="w-8 h-8 rounded-lg bg-amber-500/10 text-amber-400 flex items-center justify-center font-bold text-xs">
                                <i class="fa-solid fa-store"></i>
                            </div>
                            <div>
                                <h4 class="text-xs font-bold text-white">${escapeHtml(o.client_name)}</h4>
                                <span class="text-[10px] text-zinc-400 font-mono">${o.id} • ${dz} dz (${(dz*12)+un} cartelas)</span>
                            </div>
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="text-xs font-bold text-emerald-400 font-mono">R$ ${totalVal.toFixed(2).replace('.', ',')}</span>
                            <span class="px-2 py-0.5 rounded-full text-[10px] font-bold ${getStatusBadgeClass(o.status)}">${o.status}</span>
                            <button onclick="openReceiptModal('${o.id}')" class="text-zinc-400 hover:text-amber-400 text-xs px-2 py-1">
                                <i class="fa-solid fa-print"></i>
                            </button>
                        </div>
                    </div>
                `;
            }).join('');
        }

        function renderOrdersTable() {
            const tbody = document.getElementById('orders-table-body');
            const search = document.getElementById('search-input').value.toLowerCase();
            const statusFilter = document.getElementById('status-filter').value;
            const noMsg = document.getElementById('no-orders-msg');

            let filtered = orders.filter(o => {
                const matchSearch = (o.client_name || '').toLowerCase().includes(search) || 
                                    (o.client_doc || '').toLowerCase().includes(search) ||
                                    (o.id || '').toLowerCase().includes(search);
                const matchStatus = statusFilter === 'TODOS' || o.status === statusFilter;
                return matchSearch && matchStatus;
            });

            if (filtered.length === 0) {
                tbody.innerHTML = '';
                noMsg.classList.remove('hidden');
                return;
            }

            noMsg.classList.add('hidden');
            tbody.innerHTML = filtered.map(o => {
                const dz = parseFloat(o.qty_dozens) || 0;
                const un = parseFloat(o.qty_units) || 0;
                const pr = parseFloat(o.price_per_dozen) || 0;
                const totalCartelas = (dz * 12) + un;
                const totalValue = (dz * pr) + (un * (pr / 12));

                return `
                    <tr class="hover:bg-zinc-900/50 transition-colors">
                        <td class="px-4 py-3 font-mono text-amber-400 font-bold">${o.id}</td>
                        <td class="px-4 py-3">
                            <div class="font-bold text-white">${escapeHtml(o.client_name)}</div>
                            <div class="text-[10px] text-zinc-500">${escapeHtml(o.client_doc)}</div>
                        </td>
                        <td class="px-4 py-3">
                            <span class="font-bold text-amber-300">${dz} dz</span>
                            <span class="text-[10px] text-zinc-500 block">(${totalCartelas} cartelas / ${totalCartelas * 4} cones)</span>
                        </td>
                        <td class="px-4 py-3 font-mono font-bold text-emerald-400">
                            R$ ${totalValue.toFixed(2).replace('.', ',')}
                        </td>
                        <td class="px-4 py-3 text-zinc-400">${formatDate(o.delivery_date)}</td>
                        <td class="px-4 py-3">
                            <select onchange="changeOrderStatus('${o.id}', this.value)" class="bg-zinc-900 border border-zinc-700 text-[11px] rounded-lg px-2 py-1 font-semibold focus:outline-none ${getStatusColorText(o.status)}">
                                <option value="Pendente" ${o.status === 'Pendente' ? 'selected' : ''}>Pendente</option>
                                <option value="Em Produção" ${o.status === 'Em Produção' ? 'selected' : ''}>Em Produção</option>
                                <option value="A Caminho" ${o.status === 'A Caminho' ? 'selected' : ''}>A Caminho</option>
                                <option value="Entregue" ${o.status === 'Entregue' ? 'selected' : ''}>Entregue</option>
                            </select>
                        </td>
                        <td class="px-4 py-3 text-right space-x-1">
                            <button onclick="openReceiptModal('${o.id}')" title="Imprimir Comprovante" class="bg-zinc-800 hover:bg-amber-500/20 text-amber-400 p-2 rounded-lg">
                                <i class="fa-solid fa-print"></i>
                            </button>
                            <button onclick="deleteOrder('${o.id}')" title="Excluir" class="bg-zinc-800 hover:bg-red-500/20 text-red-400 p-2 rounded-lg">
                                <i class="fa-solid fa-trash-can"></i>
                            </button>
                        </td>
                    </tr>
                `;
            }).join('');
        }

        async function changeOrderStatus(id, newStatus) {
            const order = orders.find(o => o.id === id);
            if (order) {
                order.status = newStatus;
                if (supabaseClient) {
                    await supabaseClient.from('pedidos').update({ status: newStatus }).eq('id', id);
                }
                localStorage.setItem('buriti_brasa_orders', JSON.stringify(orders));
                updateDashboard();
                renderOrdersTable();
            }
        }

        async function deleteOrder(id) {
            if (confirm("Tem certeza que deseja excluir esta encomenda?")) {
                orders = orders.filter(o => o.id !== id);
                if (supabaseClient) {
                    await supabaseClient.from('pedidos').delete().eq('id', id);
                }
                localStorage.setItem('buriti_brasa_orders', JSON.stringify(orders));
                updateDashboard();
                renderOrdersTable();
            }
        }

        function openSupabaseModal() { document.getElementById('supabase-modal').classList.remove('hidden'); }
        function closeSupabaseModal() { document.getElementById('supabase-modal').classList.add('hidden'); }

        function saveSupabaseConfig() {
            const url = document.getElementById('supabase-url').value.trim();
            const key = document.getElementById('supabase-key').value.trim();
            if (!url || !key) return alert("Por favor, preencha a URL e a Key do Supabase.");

            localStorage.setItem('buriti_supabase_url', url);
            localStorage.setItem('buriti_supabase_key', key);
            initSupabaseFromStorage();
            fetchOrders();
            closeSupabaseModal();
        }

        function clearSupabaseConfig() {
            localStorage.removeItem('buriti_supabase_url');
            localStorage.removeItem('buriti_supabase_key');
            supabaseClient = null;
            document.getElementById('supabase-indicator').className = "w-2.5 h-2.5 rounded-full bg-amber-500";
            document.getElementById('supabase-status-text').textContent = "Supabase: Modo Local";
            closeSupabaseModal();
            fetchOrders();
        }

        function openReceiptModal(id) {
            const o = orders.find(item => item.id === id);
            if (!o) return;

            const dz = parseFloat(o.qty_dozens) || 0;
            const un = parseFloat(o.qty_units) || 0;
            const pr = parseFloat(o.price_per_dozen) || 0;
            const totalCartelas = (dz * 12) + un;
            const totalValue = (dz * pr) + (un * (pr / 12));

            document.getElementById('rec-order-id').textContent = o.id;
            document.getElementById('rec-date').textContent = formatDate(o.order_date);
            document.getElementById('rec-client-name').textContent = o.client_name;
            document.getElementById('rec-trade-name').textContent = o.client_trade_name || 'N/A';
            document.getElementById('rec-client-doc').textContent = o.client_doc;
            document.getElementById('rec-client-phone').textContent = o.client_phone;
            document.getElementById('rec-client-address').textContent = o.client_address;
            document.getElementById('rec-client-city').textContent = o.client_city;

            document.getElementById('rec-qty-dozens').textContent = `${dz} dz`;
            document.getElementById('rec-qty-cartelas').textContent = `${totalCartelas} un.`;
            document.getElementById('rec-price-dozen').textContent = `R$ ${pr.toFixed(2).replace('.', ',')}`;
            document.getElementById('rec-subtotal').textContent = `R$ ${totalValue.toFixed(2).replace('.', ',')}`;
            document.getElementById('rec-final-total').textContent = `R$ ${totalValue.toFixed(2).replace('.', ',')}`;

            document.getElementById('rec-payment').textContent = o.payment_method;
            document.getElementById('rec-delivery-date').textContent = formatDate(o.delivery_date);
            document.getElementById('rec-status').textContent = o.status;
            document.getElementById('rec-notes').textContent = o.order_notes || 'Nenhuma instrução adicional.';

            document.getElementById('receipt-modal').classList.remove('hidden');
        }

        function closeModal() { document.getElementById('receipt-modal').classList.add('hidden'); }

        function formatDate(dateStr) {
            if (!dateStr) return '-';
            const parts = dateStr.split('-');
            return parts.length === 3 ? `${parts[2]}/${parts[1]}/${parts[0]}` : dateStr;
        }

        function getStatusBadgeClass(status) {
            switch(status) {
                case 'Entregue': return 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30';
                case 'A Caminho': return 'bg-blue-500/20 text-blue-400 border border-blue-500/30';
                case 'Em Produção': return 'bg-amber-500/20 text-amber-400 border border-amber-500/30';
                default: return 'bg-red-500/20 text-red-400 border border-red-500/30';
            }
        }

        function getStatusColorText(status) {
            switch(status) {
                case 'Entregue': return 'text-emerald-400 border-emerald-500/40';
                case 'A Caminho': return 'text-blue-400 border-blue-500/40';
                case 'Em Produção': return 'text-amber-400 border-amber-500/40';
                default: return 'text-red-400 border-red-500/40';
            }
        }

        function escapeHtml(text) {
            if (!text) return '';
            return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
        }
    </script>
</body>
</html>
